from fpdf import FPDF

# Регистрируем шрифт (если нужно)
# fpdf не требует явной регистрации шрифтов, если используем стандартные
# Для использования шрифта FreeSans нужно иметь файл шрифта в соответствующей папке

# Типы компаний
type_company_data = [
    ["ID", "Название"],
    [1, "Технологическая"],
    [2, "Строительная"],
    [3, "Розничная"]
]

# Партнеры
partners_data = [
    ["ID", "Тип партнера", "Название компании", "Юридический адрес", "ИНН", "ФИО директора", "Телефон", "Email", "Рейтинг"],
    [1, 1, "ТехКорп", "Улица Тех, Москва", "1234567890", "Иван Иванов", "+7 123 456 7890", "tech@corp.com", 5],
    [2, 2, "СтроПро", "Проспект Строителей, Санкт-Петербург", "0987654321", "Петр Петров", "+7 987 654 3210", "build@pro.com", 4],
    [3, 3, "РитейлПлюс", "Бульвар Ритейла, Новосибирск", "1122334455", "Мария Сидорова", "+7 345 678 9012", "retail@plus.com", 3]
]

# Типы продуктов
product_type_data = [
    ["ID", "Название", "Коэффициент"],
    [1, "Электроника", 1.5],
    [2, "Мебель", 1.2],
    [3, "Одежда", 1.1]
]

# Продукты
product_data = [
    ["ID", "Тип", "Описание", "Артикул", "Цена", "Размер", "Класс"],
    [1, 1, "Смартфон", 12345, 300, 6.1, 1],
    [2, 2, "Офисное кресло", 67890, 150, 1.2, 2],
    [3, 3, "Футболка", 11223, 20, 0.3, 3]
]

# Продукты партнеров
partner_product_data = [
    ["ID", "ID продукта", "ID партнера", "Количество", "Дата продажи"],
    [1, 1, 1, 100, "2024-11-01"],
    [2, 2, 2, 50, "2024-11-05"],
    [3, 3, 3, 200, "2024-11-10"]
]

# Материалы
material_data = [
    ["ID", "Название", "Дефект"],
    [1, "Пластик", 0.05],
    [2, "Дерево", 0.1],
    [3, "Хлопок", 0.02]
]

# Продукты и материалы
material_product_data = [
    ["ID", "ID продукта", "ID материала"],
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

# Функция для создания PDF с таблицей
def create_pdf(data, table_name, pdf):
    pdf.add_font('FreeSans', '', './freesans.ttf', uni=True)
    # Заголовок таблицы
    pdf.set_font('FreeSans', '', 14)
    pdf.cell(200, 10, table_name, ln=True, align='C')
    pdf.ln(10)  # Отступ
    
    # Устанавливаем шрифт для данных
    pdf.set_font('FreeSans', '', 12)
    
    # Добавляем таблицу
    col_widths = [30, 60, 60, 60, 30, 40, 50, 50, 30]  # Ширина столбцов, если нужно адаптировать
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            pdf.cell(col_widths[j], 10, str(cell), border=1, align='C')
        pdf.ln()
    
    pdf.ln(10)  # Отступ перед следующей таблицей

# Создаем PDF-документ
pdf_filename = "all_tables.pdf"
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Добавляем таблицы в документ, каждая на новой странице
create_pdf(type_company_data, "Типы компаний", pdf)
pdf.add_page()
create_pdf(partners_data, "Партнеры", pdf)
pdf.add_page()
create_pdf(product_type_data, "Типы продуктов", pdf)
pdf.add_page()
create_pdf(product_data, "Продукты", pdf)
pdf.add_page()
create_pdf(partner_product_data, "Продукты партнеров", pdf)
pdf.add_page()
create_pdf(material_data, "Материалы", pdf)
pdf.add_page()
create_pdf(material_product_data, "Материалы и продукты", pdf)

# Сохраняем PDF
pdf.output(pdf_filename)

print(f"PDF файл '{pdf_filename}' был успешно создан.")
