import os
import re

def rename_files(directory):
    print(f"開始處理目錄: {directory}")
    
    # 支援的檔案類型
    valid_extensions = ('.keynote', '.pptx', '.ppt', '.key')
    
    files_found = 0
    files_renamed = 0
    
    for filename in os.listdir(directory):
        files_found += 1
        print(f"檢查檔案: {filename}")
        
        if filename.endswith(valid_extensions):
            print(f"  檔案類型有效: {filename}")
            # 使用正則表達式匹配舊的檔名格式
            match = re.match(r'(.+)_(.+)_(\d{6})$', os.path.splitext(filename)[0])
            
            if match:
                name, modifier, date = match.groups()
                new_filename = f"{date}_{name}_{modifier}{os.path.splitext(filename)[1]}"
                
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                
                try:
                    os.rename(old_path, new_path)
                    files_renamed += 1
                    print(f"  已重命名: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"  重命名失敗: {filename}. 錯誤: {str(e)}")
            else:
                print(f"  跳過: {filename} (不符合預期格式)")
        else:
            print(f"  跳過: {filename} (不支援的檔案類型)")
    
    print(f"\n總結:")
    print(f"檢查的檔案總數: {files_found}")
    print(f"重命名的檔案數: {files_renamed}")

if __name__ == "__main__":
    directory = input("請輸入要處理的目錄路徑: ")
    rename_files(directory)
    
    input("按Enter鍵結束程式...")