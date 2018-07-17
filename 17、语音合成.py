#系统客户端包
import win32com.client

dehua = win32com.client.Dispatch("SAPI.SPVOICE")
dehua.Speak("turo is a good man")
