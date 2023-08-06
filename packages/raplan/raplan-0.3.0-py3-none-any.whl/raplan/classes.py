"""Dataclasses to use and configure planning and scheduling with."""

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Optional, Union

from serde import ExternalTagging, field, serde


def _is_empty(lst: Union[list, dict, set]) -> bool:
    """Check whether a list is empty."""
    return len(lst) == 0


def compound_probability(probabilities: Iterable[float]) -> float:
    """Compound CDF value of multiple contributions."""
    return max(0.0, 1.0 - math.prod(1 - p for p in probabilities))


class Distribution(ABC):
    """Abstract base class for distributions."""

    def cdf(self, x: Union[int, float] = 1.0) -> float:
        """Cumulative probability density function of this distribution."""
        if x < 0:
            return 0.0
        return self._cdf(x)

    @abstractmethod
    def _cdf(self, x: Union[int, float] = 1.0) -> float:
        """Cumulative probability density function of this distribution."""


@serde
@dataclass
class ContinuousDistribution(Distribution):
    """A continuous rate distribution."""

    rate: Union[int, float] = 1.0

    def _cdf(self, x: Union[int, float] = 1.0) -> float:
        return min(1.0, float(x * self.rate))


@serde
@dataclass
class WeibullDistribution(Distribution):
    """Weibull distribution (2-parameter).

    Arguments:
        alpha: Shape parameter.
        mtbf: Mean time between failure.
    """

    alpha: Union[int, float] = 2.0
    mtbf: Union[int, float] = 10.0

    @property
    def beta(self) -> float:
        """Weibull scale parameter."""
        return self.mtbf / math.gamma(1.0 + 1.0 / self.alpha)

    def _cdf(self, x: Union[int, float] = 1.0) -> float:
        return 1.0 - math.exp(-((x / self.beta) ** self.alpha))


Distributions = Union[WeibullDistribution, ContinuousDistribution]


@serde
@dataclass
class Task:
    """Maintenance task to apply to a component.

    Arguments:
        name: Name for this action.
        rejuvenation: Rejuvenation factor between [0.0-1.0]. Percentage of age that is
            regained. Therefore, 1.0 would mean a full replacement.
        duration: Duration of the maintenance. Usually in years.
        cost: Cost of the maintenance. Usually expressed in a currency or equivalent.
    """

    name: Optional[str] = field(default=None, skip_if_default=True)
    rejuvenation: Union[int, float] = 1.0
    duration: Union[int, float] = 1.0
    cost: Union[int, float] = 1.0


@serde
@dataclass
class Maintenance:
    """Maintenance task scheduled at a point in time.

    Arguments:
        name: Name of this maintenance task.
        task: Task information.
        time: Time at which this maintenance is scheduled.
    """

    name: Optional[str] = field(default=None, skip_if_default=True)
    task: Task = field(default_factory=Task)
    time: Union[int, float] = 1.0


@serde(tagging=ExternalTagging)
@dataclass
class Component:
    """Component with a failure distribution.

    Arguments:
        name: Name of this component.
        age: Starting age offset (usually in years).
        distribution: Failure distribution to use.
        maintenance: List of maintenance tasks that should be applied over this
            component's lifespan.
    """

    name: Optional[str] = field(default=None, skip_if_default=True)
    age: Union[int, float] = 0.0
    distribution: Distributions = field(default_factory=WeibullDistribution)
    maintenance: list[Maintenance] = field(default_factory=list, skip_if=_is_empty)

    def get_ordered_maintenance(self) -> list[Maintenance]:
        """Maintenance tasks sorted in time."""
        return sorted(self.maintenance, key=lambda m: m.time)

    def cfp(self, x: Union[int, float] = 1.0) -> float:
        """Cumulative failure probability density function incorporating maintenance."""
        return self.distribution.cdf(self.get_age_at(x))

    def get_age_at(self, x: Union[int, float] = 1.0) -> float:
        """Effective age at a point in time given the currently set schedule."""
        age = float(self.age)
        last_time = 0.0
        for m in self.get_ordered_maintenance():
            if m.time > x:
                # Maintenance is yet to happen.
                break
            # Apply rejuvenation with the then actual age.
            age = (age + m.time - last_time) * (1.0 - m.task.rejuvenation)
            last_time = m.time
        # Add remaining time since last maintenance.
        age += x - last_time
        return age

    def schedule_maintenance(self, maintenance: Maintenance):
        """Schedule maintenance for a single or all system's component or all
        components.

        Arguments:
            maintenance: Maintenance to schedule.
        """
        self.maintenance.append(maintenance)


@serde
@dataclass
class System:
    """A system consisting of multiple components.

    Arguments:
        name: Name of this system.
        components: Components of this system.
    """

    name: Optional[str] = field(default=None, skip_if_default=True)
    components: list[Component] = field(default_factory=list, skip_if=_is_empty)

    def cfp(self, x: Union[int, float] = 1.0) -> float:
        """Cumulative failure probability density function as the sum of its
        components' respective function incorporating maintenance.
        """
        if len(self.components):
            return compound_probability(c.cfp(x) for c in self.components)
        else:
            return 0.0

    def get_ordered_maintenance(self) -> list[Maintenance]:
        """Get all maintenance ordered in time."""
        return sorted(
            [m for c in self.components for m in c.maintenance], key=lambda m: m.time
        )

    def get_component(self, name: str) -> Component:
        """Get a component by name."""
        for c in self.components:
            if c.name == name:
                return c
        raise KeyError(f"Component with name '{name}' does not exist in this system.")

    def schedule_maintenance(
        self, maintenance: Maintenance, component: Optional[str] = None
    ):
        """Schedule maintenance for a single or all system's component or all
        components.

        Arguments:
            maintenance: Maintenance to schedule.
            component: Component name. If kept `None`, it will be applied to all.
        """
        if component is None:
            for c in self.components:
                c.schedule_maintenance(maintenance)
        else:
            self.get_component(component).schedule_maintenance(maintenance)


@serde
@dataclass
class Horizon:
    """Planning and scheduling horizon.

    Arguments:
        start: Start of the planning horizon.
        end: End of the planning horizon. Optional, as it is otherwise derived from the
            final task in the schedule.
    """

    start: Union[int, float] = 0.0
    end: Optional[Union[int, float]] = field(default=None, skip_if_default=True)

    def get_range(self, steps: int, zero_based: bool = True) -> list[Union[int, float]]:
        """Range between start and end (inclusive) in the given number of steps."""
        if self.end is None:
            raise ValueError("Can't calculate a range with no horizon end value.")
        step_size = (self.end - self.start) / steps
        start = type(self.start)(0) if zero_based else self.start
        return [start + i * step_size for i in range(steps + 1)]


@serde
@dataclass
class Project:
    """Planning and scheduling project."""

    name: Optional[str] = field(default=None, skip_if_default=True)
    horizon: Horizon = field(default_factory=Horizon)
    systems: list[System] = field(default_factory=list, skip_if=_is_empty)

    def get_horizon_end(self) -> float:
        """Get the end of the planning horizon or last maintenance task."""
        if self.horizon.end is None:
            end = 0.0
            try:
                end = max(
                    m.time
                    for s in self.systems
                    for c in s.components
                    for m in c.maintenance
                )
            except ValueError:
                pass  # arg is an empty sequency: end = 0.0
            finally:
                return end
        return self.horizon.end

    def cfp(self, x: Union[int, float] = 1.0) -> float:
        """Cumulative failure probability density function as the sum of its
        systems' respective function incorporating maintenance.
        """
        if len(self.systems):
            return compound_probability(s.cfp(x) for s in self.systems)
        else:
            return 0.0

    def get_ordered_maintenance(self) -> list[Maintenance]:
        """Get all maintenance ordered in time."""
        return sorted(
            [m for s in self.systems for c in s.components for m in c.maintenance],
            key=lambda m: m.time,
        )

    def get_system(self, name: str) -> System:
        """Get a component by name."""
        for s in self.systems:
            if s.name == name:
                return s
        raise KeyError(f"System with name '{name}' does not exist in this project.")

    def schedule_maintenance(
        self,
        maintenance: Maintenance,
        system: Optional[str] = None,
        component: Optional[str] = None,
    ):
        """Schedule maintenance for a single or all system's component or all
        components.

        Arguments:
            maintenance: Maintenance to schedule.
            system: System name. If kept `None`, it will be applied to all.
            component: Component name. If kept `None`, it will be applied to all.
        """
        if system is None:
            for s in self.systems:
                s.schedule_maintenance(maintenance, component=component)
        else:
            self.get_system(system).schedule_maintenance(
                maintenance, component=component
            )

    def get_schedule(self) -> "Schedule":
        """Get a fully generated schedule."""
        return Schedule(
            tasks=[
                ScheduledTask(
                    m.task.name,
                    rejuvenation=m.task.rejuvenation,
                    duration=m.task.duration,
                    cost=m.task.cost,
                    system=s.name,
                    component=c.name,
                    time=m.time,
                )
                for s in self.systems
                for c in s.components
                for m in c.maintenance
            ]
        )


@serde
@dataclass
class ScheduledTask:
    """A task with full detail regarding its system, component and maintenance info.

    Arguments:
        name: Name for this action.
        rejuvenation: Rejuvenation factor between [0.0-1.0]. Percentage of age that is
            regained. Therefore, 1.0 would mean a full replacement.
        duration: Duration of the maintenance. Usually in years.
        cost: Cost of the maintenance. Usually expressed in a currency or equivalent.
        system: Name of the system to which this maintenance is applied.
        component: Name of the component to which this maintenance is applied.
        time: Time at which this maintenance is scheduled.
    """

    name: Optional[str] = field(default=None, skip_if_default=True)
    rejuvenation: Union[int, float] = 1.0
    duration: Union[int, float] = 1.0
    cost: Union[int, float] = 1.0
    system: Optional[str] = field(default=None, skip_if_default=True)
    component: Optional[str] = field(default=None, skip_if_default=True)
    time: Union[str, float] = 1.0


@serde
@dataclass
class Schedule:
    """A full maintenance schedule.

    Arguments:
        tasks: Scheduled tasks.
    """

    tasks: list[ScheduledTask] = field(default_factory=list, skip_if=_is_empty)

    def get_ordered_maintenance(self) -> list[ScheduledTask]:
        """Get all tasks ordered in time."""
        return sorted(self.tasks, key=lambda t: t.time)
