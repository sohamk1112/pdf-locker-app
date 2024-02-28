from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileReader, PdfReader, PdfWriter

def select_source_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        source.set(file_path)
        target.set(file_path[:-4] + "_locked.pdf")

def protect_pdf():
    input_pdf_path = source.get()
    output_pdf_path = target.get()

    if not input_pdf_path or not output_pdf_path:
        messagebox.showerror("Error", "Please select source and target PDF files.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf_path)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(user_pwd=password, use_128bit=True)

    with open(output_pdf_path, 'wb') as encrypted_pdf_file:
        pdf_writer.write(encrypted_pdf_file)

    messagebox.showinfo("Success", "PDF encrypted and saved successfully.")

root = Tk()
root.title("PDF Locker App")
root.geometry("700x400")
root.resizable(True, True)

frame = Frame(root)
frame.pack(padx=20, pady=20)

source = StringVar()
target = StringVar()

Label(frame, text="Source File PDF:", font="arial 10 bold").grid(row=0, column=0, sticky=W)
entry1 = Entry(frame, width=30, textvariable=source, font='arial 15', bd=1)
entry1.grid(row=0, column=1)
Button(frame, text="Select", command=select_source_file).grid(row=0, column=2)

Label(frame, text="Target PDF file:", font="arial 10 bold").grid(row=1, column=0, sticky=W)
entry2 = Entry(frame, width=30, textvariable=target, font='arial 15', bd=1)
entry2.grid(row=1, column=1)

Label(frame, text="Enter Password:", font="arial 10 bold").grid(row=2, column=0, sticky=W)
password_entry = Entry(frame, width=30, font='arial 15', bd=1)
password_entry.grid(row=2, column=1)

Button(frame, text="Lock PDF", command=protect_pdf).grid(row=3, column=1, pady=20)

root.mainloop()
