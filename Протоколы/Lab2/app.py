from docxtpl import DocxTemplate
doc = DocxTemplate("shablon.docx")
content = { 
    'institut': "Институт",
    'kafedra': "Кафедра",
    'number': 1,
    'name': 'Название лабораторной',
    'group': 'Номер группы',
    'student': "ФИО студента",
    'prepod': "ФИО преподавателя"
}
doc.render(content)
doc.save("final_shablon.docx")

