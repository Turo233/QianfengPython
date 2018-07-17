import win32com
import win32com.client

def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Applicatino")
    ppt.Visible = True


    #增加一个文件
    pptFile = ppt.Presentations.Add()

    #创建页
    pag1 = pptFile.Slides.Add()
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "turo"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "turo is a good man"

    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()



path = r"‪E:\1编程\千锋python\Code\47、ppt自动化办公\a.ppt"
makePPT(path)
