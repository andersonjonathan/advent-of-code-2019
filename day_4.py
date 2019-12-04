def main():
    passwords = [pw for pw in range(172930, 683082) if
                 str(pw)[0] <= str(pw)[1] <= str(pw)[2] <= str(pw)[3] <= str(pw)[4] <= str(pw)[5]]
    passwords = [pw for pw in passwords if str(pw)[0] == str(pw)[1] or
                 str(pw)[1] == str(pw)[2] or
                 str(pw)[2] == str(pw)[3] or
                 str(pw)[3] == str(pw)[4] or
                 str(pw)[4] == str(pw)[5]]
    passwords = [pw for pw in passwords if
                 (str(pw)[0] == str(pw)[1] and str(pw)[1] != str(pw)[2]) or
                 (str(pw)[1] == str(pw)[2] and str(pw)[0] != str(pw)[1] and str(pw)[2] != str(pw)[3]) or
                 (str(pw)[2] == str(pw)[3] and str(pw)[1] != str(pw)[2] and str(pw)[3] != str(pw)[4]) or
                 (str(pw)[3] == str(pw)[4] and str(pw)[2] != str(pw)[3] and str(pw)[4] != str(pw)[5]) or
                 (str(pw)[4] == str(pw)[5] and str(pw)[3] != str(pw)[4])]
    print(len(passwords))


if __name__ == '__main__':
    main()
