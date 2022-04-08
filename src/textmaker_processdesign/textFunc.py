import tkinter


def make_process_text(btn_name, target_data_nm):
    if target_data_nm == '':
        target_data_nm = "★★값넣어★★"

    data = ""
    t_save = "- ‘저장’ 버튼을 클릭하면 신규로 등록하거나 수정된 정보가 저장되고 삭제 했던 항목은 완전히 삭제된다.\n"
    t_search = "- ‘조회’ 버튼을 클릭하면 입력한 검색 조건에 맞게 화면에 표시된다.\n"
    t_insert = "- ‘신규’ 버튼을 클릭하면 " + target_data_nm + " 등록할 수 있는 팝업이 생성된다.\n"
    t_update = "- ‘수정’ 버튼을 클릭하면 " + target_data_nm + " 수정할 수 있는 팝업이 생성된다.\n"
    t_delete = "- ‘삭제’ 버튼을 클릭하면 선택한 정보가 삭제된다. 완전히 삭제된 상태는 아니다.\n"
    t_download = "- ‘엑셀다운로드’ 버튼을 클릭하면 조회된 정보들이 엑셀파일로 다운로드 된다.\n"
    t_download_outline = "- ‘엑셀양식다운로드‘ 버튼을 클릭하면 업로드할 수 있는 엑셀양식이 다운로드된다.\n"
    t_upload = "- ‘엑셀업로드’ 버튼을 클릭하면 업로드한 엑셀양식에 따라 작성된 정보가 신규로 저장된다.\n"
    t_add = "- ‘추가’ 버튼을 클릭하면 " + target_data_nm + " 등록할 수 있는 행이 추가된다.\n"



    if btn_name == '저장':
        data = data + t_save
    elif btn_name == '조회':
        data = data + t_search
    elif btn_name == '신규':
        data = data + t_insert
    elif btn_name == '수정':
        data = data + t_update
    elif btn_name == '삭제':
        data = data + t_delete
    elif btn_name == '엑셀다운':
        data = data + t_download
    elif btn_name == '양식다운':
        data = data + t_download_outline
    elif btn_name == '엑셀업로드':
        data = data + t_upload
    elif btn_name == '추가':
        data = data + t_add
    else:
        data = "안됨"

    return data


