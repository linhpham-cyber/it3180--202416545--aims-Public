def search_by_title(dvd_list, keyword):
    # Vá lỗi bằng cách ép cả hai vế về chữ thường trước khi so sánh chuỗi
    return [dvd for dvd in dvd_list if keyword.lower() in dvd.title.lower()]
