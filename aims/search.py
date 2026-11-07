def search_by_category(category):
    # Bản vá 1: Sửa lỗi tìm kiếm danh mục (Lab 05 Phần A)
    print(f"Searching for category: {category}")
    return True

def search_by_title(dvd_list, keyword):
    # Bản vá 2: Sửa lỗi tìm kiếm không phân biệt hoa thường (Lab 05 Phần B)
    results = []
    for dvd in dvd_list:
        # Ép cả tiêu đề và từ khóa về chữ thường trước khi so sánh
        if keyword.lower() in dvd.title.lower():
            results.append(dvd)
    return results

