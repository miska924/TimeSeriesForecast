# Code adapted from StackOverflow
# https://ru.stackoverflow.com/questions/840239/%D0%9A%D0%B0%D0%BA-%D0%B2%D0%BD%D0%B5%D0%B4%D1%80%D0%B8%D1%82%D1%8C-%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D0%BF%D0%BE%D1%82%D0%BE%D1%87%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B2-pyqt

import sys
import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

class WorkerSignals(QObject):
    ''' Определяет сигналы, доступные из рабочего рабочего потока Worker(QRunnable).'''

    finish   = pyqtSignal()
    error    = pyqtSignal(tuple)
    result   = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    ''' Наследует от QRunnable, настройки рабочего потока обработчика, сигналов и wrap-up. '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Хранить аргументы конструктора (повторно используемые для обработки)
        self.fn      = fn
        self.args    = args
        self.kwargs  = kwargs
        self.signals = WorkerSignals()
        self.stop    = False

        #== Добавьте обратный вызов в наши kwargs ====================================###
        # kwargs['progress_callback'] = self.signals.progress
        # print("kwargs['progress_callback']->`{}`\n".format(kwargs['progress_callback']))

    @pyqtSlot()
    def run(self):
        # Получите args/kwargs здесь; и обработка с их использованием
        try:
            result = self.fn(*self.args, **self.kwargs) 
            if not result:
                return
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:  # если ошибок не была, испускаем сигнал .result и передаем результат `result`
            self.signals.result.emit(result)      # Вернуть результат обработки
        finally:
            self.signals.finish.emit()            # Done / Готово
