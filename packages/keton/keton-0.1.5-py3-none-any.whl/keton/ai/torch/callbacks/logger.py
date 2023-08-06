import tqdm

from torch.utils.tensorboard import SummaryWriter

from .common import Callback


__all__ = [
    "TqdmTrainLogger",
    "TensorBoard"
]


class TqdmTrainLogger(Callback):

    def __init__(self,
                 log_on: str = "step") -> None:
        super().__init__()

        if log_on == "step":
            self._log_on_step = True
        elif log_on == "epoch":
            self._log_on_step = False
        else:
            raise ValueError(f"Unknown log mode '{log_on}'")

        self._pbar = None
        self._description = None
        self._epochs = 1
        self._steps_per_epoch = 1

    def set_params(self, params: dict) -> None:
        self._epochs = params.get("epochs", 1)
        self._steps_per_epoch = params.get("steps_per_epoch", 1)
        self._description = params.get("description", None)

    def on_train_begin(self) -> None:
        if not self._log_on_step:
            self._pbar = tqdm.tqdm(total=self._epochs)
            self._pbar.set_description(self._description)

    def on_epoch_begin(self, epoch: int) -> None:
        if self._log_on_step:
            self._pbar = tqdm.tqdm(total=self._steps_per_epoch)
            self._pbar.set_description(f"Epoch {epoch}/{self._epochs}")

    def on_train_batch_end(self, batch: int, metrics: dict) -> None:
        if self._log_on_step:
            self._pbar.update(1)
            self._pbar.set_postfix_str(self._metrics_to_str(metrics))

    def on_train_epoch_end(self, epoch: int, metrics: dict) -> None:
        if not self._log_on_step:
            self._pbar.update(1)
            self._pbar.set_postfix_str(self._metrics_to_str(metrics))

    def on_eval_end(self, metrics: dict) -> None:
        self._pbar.set_postfix_str(
            f"{self._pbar.postfix}, {self._metrics_to_str(metrics, 'val')}")

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        if self._log_on_step:
            self._pbar.close()

    def on_train_end(self) -> None:
        if not self._log_on_step:
            self._pbar.close()

    @staticmethod
    def _metrics_to_str(metrics: dict, prefix: str = None) -> str:
        pairs = []
        for k, v in metrics.items():
            if v.dim() == 1:
                v = ",".join(map(lambda x: f"{x:.5f}", v))
            else:
                v = f"{v:.7f}"
            if prefix:
                k = f"{prefix}_{k}"
            pairs.append(f"{k}={v}")
        return ", ".join(pairs)


class TensorBoard(Callback):

    def __init__(self,
                 log_dir=None,
                 comment='',
                 purge_step=None,
                 max_queue=10,
                 flush_secs=120,
                 filename_suffix='',
                 **kwargs) -> None:
        super().__init__()
        self._sum_writter = SummaryWriter(
            log_dir=log_dir, comment=comment, purge_step=purge_step,
            max_queue=max_queue, flush_secs=flush_secs,
            filename_suffix=filename_suffix,
            **kwargs
        )

    def on_epoch_end(self, epoch: int, metrics: dict) -> None:
        for k, v in metrics.items():
            keys = k.split("_", 1)
            if len(keys) == 1:
                self._sum_writter.add_scalar(f"{keys[0]}/train", v, global_step=epoch)
            else:
                self._sum_writter.add_scalar(f"{keys[1]}/{keys[0]}", v, global_step=epoch)