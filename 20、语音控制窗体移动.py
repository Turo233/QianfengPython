from win32com.client import constants
import os
import win32com.client
import pythoncom
import win32con
import win32gui

class SpeechRecognition:
    def __init__(self, wordToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SPVOICE")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule",
        constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for
        word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("说：", newResult.PhraseInfo.GetText())
        s = newResult.PhraseInfo.GetText()
        if s == "记事本":
            QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
            win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 200, 0,
                600, 400, win32con.SWP_SHOWWINDOW)
        if s == "向右":
            QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
            win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 200, 0,
                600, 400, win32con.SWP_SHOWWINDOW)
            win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 400, 0,
                600, 400, win32con.SWP_SHOWWINDOW)
if __name__ == "__main__":
    wordsToAdd = ["记事本", "向右", "停", "画图板", "写字板", "设置", "关闭记事本"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
