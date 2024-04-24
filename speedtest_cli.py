from tkinter import *
import speedtest_cli

def speedcheck():
    sp = speedtest_cli.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x500")
sp.config(bg="#f0f0f0")  # Soft gray background

lab = Label(sp, text="Internet Speed", font=("Segoe UI", 30, "bold"), bg="#d3d3d3", fg="black")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Segoe UI", 20, "bold"), bg="#d3d3d3", fg="black")
lab.place(x=60, y=130, height=30, width=380)

lab_down = Label(sp, text="00", font=("Segoe UI", 20, "bold"), bg="#d3d3d3", fg="black")
lab_down.place(x=60, y=170, height=30, width=380)

lab = Label(sp, text="Upload Speed", font=("Segoe UI", 20, "bold"), bg="#d3d3d3", fg="black")
lab.place(x=60, y=220, height=30, width=380)

lab_up = Label(sp, text="00", font=("Segoe UI", 20, "bold"), bg="#d3d3d3", fg="black")
lab_up.place(x=60, y=260, height=30, width=380)

button = Button(sp, text="Check Speed", font=("Segoe UI", 20, "bold"), relief=RAISED, bg="#c0c0c0", command=speedcheck)
button.place(x=60, y=310, height=50, width=380)

sp.mainloop()
