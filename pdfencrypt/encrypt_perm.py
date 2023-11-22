from pikepdf import Pdf, Permissions, Encryption, PasswordError


with Pdf.open('me.pdf') as pdf:
    no_edit = Permissions(modify_annotation=False,
                          modify_assembly=False,
                          modify_form=False,
                          modify_other=False,
                          print_lowres=False,
                          print_highres=False,
                          extract=False)
    pdf.save('me2.pdf', encryption=Encryption(user='', owner='123456', allow=no_edit))
