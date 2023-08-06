from typing import Any, Callable

import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler

from .common import Callback


__all__ = [
    "EarlyStopping",
    "ReduceLROnPlateau",
    "LRScheduler",
    "CosineAnnealingLR",
    "CosineAnnealingWarmRestarts",
    "CyclicLR"
]


class EarlyStopping(Callback):

    def __init__(self,
                 monitor: str = "val_loss",
                 mode: str = "min",
                 threshold: float = 0.0001,
                 threshold_mode: str = "rel",
                 patience: int = 5,
                 restore_best: bool = False,
                 verbose: bool = True) -> None:
        super().__init__()
        if mode not in {"min", "max"}:
            raise ValueError(f"monitor mode '{mode}' is not supported")
        if threshold_mode not in {"rel", "abs"}:
            raise ValueError(f"threshold mode '{threshold_mode}' is not supported")
        self._monitor = monitor
        self._mode = mode
        self._threshold = abs(threshold)
        self._threshold_mode = threshold_mode
        self._patience = patience
        self._restore_best = restore_best
        self._verbose = verbose
        self._last_epoch = 0
        self._last_value = None
        self._controls = None
        self._best_weights = None

    def set_params(self, params: dict) -> None:
        self._controls = params.get("controls")

    def _is_better(self, v1: Any, v2: Any) -> bool:
        delta = (v1 - v2) if self._mode == "min" else (v2 - v1)
        if self._threshold_mode == "rel":
            delta = delta / abs(v1)
        return delta >= self._threshold

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        value = metrics[self._monitor]

        if epoch == 1 or self._is_better(self._last_value, value):
            self._last_epoch = epoch
            self._last_value = value
            if self._restore_best:
                self._best_weights = {k: v.cpu().clone().detach() for k, v in self._model.state_dict().items()}
        elif epoch - self._last_epoch > self._patience:
            if self._verbose:
                print(f"Epoch {epoch:05d}: stopping due to no improvement from epoch {self._last_epoch:05d}.")
            self._controls.stop_training = True

    def on_train_end(self) -> None:
        if self._restore_best:
            if self._verbose:
                print(f"Restoring best weights saved from epoch {self._last_epoch:05d}")
            self._model.load_state_dict(self._best_weights)


class ReduceLROnPlateau(Callback):

    def __init__(self,
                 monitor: str = "val_loss",
                 mode: str = "min",
                 factor: float = 0.1,
                 patience: int = 10,
                 threshold: float = 0.0001,
                 threshold_mode: str = "rel",
                 cooldown: int = 0,
                 min_lr: float = 0.,
                 eps: float = 1e-08,
                 verbose: bool = True) -> None:
        super().__init__()
        self._monitor = monitor
        self._mode = mode
        self._factor = factor
        self._patience = patience
        self._threshold = threshold
        self._threshold_mode = threshold_mode
        self._cooldown = cooldown
        self._min_lr = min_lr
        self._eps = eps
        self._verbose = verbose
        self._lr_scheduler: lr_scheduler.ReduceLROnPlateau = None

    def set_optimizer(self, optimizer: optim.Optimizer) -> None:
        self._lr_scheduler = lr_scheduler.ReduceLROnPlateau(
            optimizer=optimizer,
            mode=self._mode,
            factor=self._factor,
            patience=self._patience,
            threshold=self._threshold,
            threshold_mode=self._threshold_mode,
            cooldown=self._cooldown,
            min_lr=self._min_lr,
            eps=self._eps,
            verbose=self._verbose
        )
        return super().set_optimizer(optimizer)

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        value = metrics[self._monitor]
        self._lr_scheduler.step(value)


class CosineAnnealingLR(Callback):

    def __init__(self,
                 T_max: int,
                 eta_min: float = 0,
                 verbose: bool = True) -> None:
        super().__init__()
        self._T_max = T_max
        self._eta_min = eta_min
        self._verbose = verbose
        self._lr_scheduler: lr_scheduler.CosineAnnealingLR = None

    def set_optimizer(self, optimizer: optim.Optimizer) -> None:
        self._lr_scheduler = lr_scheduler.CosineAnnealingLR(
            optimizer=optimizer,
            T_max=self._T_max,
            eta_min=self._eta_min,
            verbose=self._verbose
        )
        return super().set_optimizer(optimizer)

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        self._lr_scheduler.step()


class CosineAnnealingWarmRestarts(Callback):

    def __init__(self,
                 T_0: int,
                 T_mult: int = 1,
                 eta_min: float = 0,
                 verbose: bool = True) -> None:
        super().__init__()
        self._T_0 = T_0
        self._T_mult = T_mult
        self._eta_min = eta_min
        self._verbose = verbose
        self._lr_scheduler: lr_scheduler.CosineAnnealingWarmRestarts = None

    def set_optimizer(self, optimizer: optim.Optimizer) -> None:
        self._lr_scheduler = lr_scheduler.CosineAnnealingWarmRestarts(
            optimizer=optimizer,
            T_0=self._T_0,
            T_mult=self._T_mult,
            eta_min=self._eta_min,
            verbose=self._verbose
        )
        return super().set_optimizer(optimizer)

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        self._lr_scheduler.step()


class CyclicLR(Callback):

    def __init__(self,
                 base_lr: float,
                 max_lr: float,
                 step_size_up: int = 2000,
                 step_size_down: int = None,
                 mode: str = 'triangular',
                 gamma: float = 1.,
                 scale_fn: Callable = None,
                 scale_mode: str = 'cycle',
                 cycle_momentum: bool = True,
                 base_momentum: float = 0.8,
                 max_momentum: float = 0.9,
                 verbose: bool = False) -> None:
        super().__init__()
        self._base_lr = base_lr
        self._max_lr = max_lr
        self._step_size_up = step_size_up
        self._step_size_down = step_size_down
        self._mode = mode
        self._gamma = gamma
        self._scale_fn = scale_fn
        self._scale_mode = scale_mode
        self._cycle_momentum = cycle_momentum
        self._base_momentum = base_momentum
        self._max_momentum = max_momentum
        self._verbose = verbose
        self._lr_scheduler = None

    def set_optimizer(self, optimizer: optim.Optimizer) -> None:
        self._lr_scheduler = lr_scheduler.CyclicLR(
            optimizer=optimizer,
            base_lr=self._base_lr,
            max_lr=self._max_lr,
            step_size_up=self._step_size_up,
            step_size_down=self._step_size_down,
            mode=self._mode,
            gamma=self._gamma,
            scale_fn=self._scale_fn,
            scale_mode=self._scale_mode,
            cycle_momentum=self._cycle_momentum,
            base_momentum=self._base_momentum,
            max_momentum=self._max_momentum,
            verbose=self._verbose
        )
        return super().set_optimizer(optimizer)

    def on_train_batch_end(self, batch: int, metrics: dict) -> None:
        self._lr_scheduler.step()


class LRScheduler(Callback):

    def __init__(self,
                 scheduler_type,
                 call_on: str = "epoch",
                 **scheduler_params) -> None:
        super().__init__()
        self._call_on_epoch = (call_on == "epoch")
        self._scheduler_type = scheduler_type
        self._scheduler_params = scheduler_params
        self._scheduler: scheduler_type = None

    def set_optimizer(self, optimizer: optim.Optimizer) -> None:
        self._scheduler = self._scheduler_type(optimizer, **self._scheduler_params)
        return super().set_optimizer(optimizer)

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        if self._call_on_epoch:
            self._scheduler.step()

    def on_train_batch_end(self, batch: int, metrics: dict) -> None:
        if not self._call_on_epoch:
            self._scheduler.step()
