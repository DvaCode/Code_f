
import os.path
import shutil



if __name__ == "__main__" :
    # 해당하는 폴더 위치 주소를 입력받기
    # 입력받은 주소가 유효한지 확인
    # 해당하는 폴더에 파일이 있는 지 확인
    # 파일 분류
    # 비교 대조 같은 파일 있는지 확인
    # if it does exits then move the files
    # if it does not, nothing to do, just leave the files in the directory
    # 작업 완료했다는 메시지 띄우기
    print("File arrange Program Start!!")

    while(1):
        menu_num = int(input("1. 파일정리, 2. 해당 폴더 파일 목록 출력, 3. 종료\n입력 : "))

        if(menu_num == 1):
            print("파일 정리 시작")
            target_file_path = input("작업할 파일 주소를 입력하세요<< ")
            destination_file_path = input("옮길 파일 주소를 입력하세요<< ")
            if not os.path.exists(target_file_path):
                print(f"입력하신 해당 폴더 f{target_file_path}에는 파일이 없습니다.")
                exit(1)
            print(f"입력한 작업할 파일 주소는 {target_file_path}이고 옮길 파일 주소는 {destination_file_path}입니다.")

            print("작업을 실행합니다.\n")
            input('...')
            file_list_src1 = []  # 비교 기준
            file_list_src2 = []  # 비교 대상
            file_path = os.listdir(target_file_path)
            for file_name_list in file_path:
                if 'json' in file_name_list:
                    file_list_src1.append(file_name_list)
                elif 'txt' in file_name_list:
                    file_list_src2.append(file_name_list)
            find_unarranged_the_files = False
            for file_name_list1 in file_list_src1:
                # 같은 파일명 존재
                temp_str = file_name_list1.split(".")[0]
                print(f"json File name : {temp_str}")
                for file_name_list2 in file_list_src2:
                    temp_str_2 = file_name_list2.split(".")[0]
                    if temp_str == temp_str_2:
                        print(f"txt File name : {temp_str_2}")
                        shutil.move(target_file_path + '/' + file_name_list1, destination_file_path + '/' + file_name_list1)
                        shutil.move(target_file_path + '/' + file_name_list2, destination_file_path + '/' + file_name_list2)
                        print(f'같은 파일 찾았음!! {file_name_list1}.')
                        find_unarranged_the_files = True
                # 존재 하지 않으면 Continue:
            print("Process Done!!")
            input('...')
            if (find_unarranged_the_files == False):
                print("작업할 파일들을 찾지 못했습니다.\n")

        elif(menu_num == 3):
            print("종료")
            break
        elif(menu_num == 2):
            print("해당 폴더 파일목록 출력")
            target_file_path = input("출력할 폴더 주소 입력 : ")
            if not os.path.exists((target_file_path)):
                exit(1)
            print(f"입력한 폴더 주소는 {target_file_path} 입니다.")
            target_file_list = []
            file_path = os.listdir(target_file_path)
            for file_list in file_path:
                print(file_list)
        else:
            print("메뉴에 있는 번호를 입력해주세요.")

    print('Process Complete')
    input('...')




