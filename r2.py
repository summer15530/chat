def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None
    巨大旅遊周效宏_word_count = 0
    巫Sam_word_count = 0
    巨大旅遊周效宏_sticker_count = 0
    巫Sam_sticker_count = 0
    巨大旅遊周效宏_image_count = 0
    巫Sam_image_count = 0
    for line in lines:
        s = line.split('\t')
        time = s[0]
        name = s[1]
        if name == '巨大旅遊周效宏':
            if s[2] == '[貼圖]':
                巨大旅遊周效宏_sticker_count += 1
            elif s[2] == '[圖片]':
                巨大旅遊周效宏_image_count += 1

            else:                
                for m in s[2:]:
                    巨大旅遊周效宏_word_count += len(m)
        elif name == '巫Sam':
            if s[2] == '[貼圖]':
                巫Sam_sticker_count += 1
            elif s[2] == '[圖片]':
                巫Sam_image_count += 1
            else:
                for m in s[2:]:                
                    巫Sam_word_count += len(m)

    print('巨大旅遊周效宏說了',巨大旅遊周效宏_word_count,'個字')
    print('巫Sam說了',巫Sam_word_count,'個字')
    print('巨大旅遊周效宏使用了貼圖',巨大旅遊周效宏_sticker_count, '次' )  
    print('巫Sam使用了貼圖',巫Sam_sticker_count, '次' )            
    print('巨大旅遊周效宏使用了圖片',巨大旅遊周效宏_image_count, '次' )  
    print('巫Sam使用了圖片',巫Sam_image_count, '次' )
   
    

    return   
 
    
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')       


def main():
    lines = read_file('[LINE] Sam.txt') 
    lines = convert(lines)
    #write_file('output.txt', lines)   


main()