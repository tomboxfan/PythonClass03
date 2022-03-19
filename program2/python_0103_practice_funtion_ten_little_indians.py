'''
Requirement:
Define 2 functions to output the following lyrics:

One little, two little, three little Indians
Four little, five little, six little Indians
Seven little, eight little, nine little Indians
Ten little Indian boys.

Ten little, nine little, eight little Indians
Seven little, six little, five little Indians
Four little, three little, two little Indians
One little Indian boy.

In the above 8 lines, 6 of them are quite similar, 2 of them are similar.

The name of the 2 functions are:
lyric_main(<You_define_parameter_here>)
lyric_end(<You_define_parameter_here>)
HINT: You can define multiple parameters inside the parentheses, separated by ','
'''































def lyric_main(s1, s2, s3):
    print(f"{s1} little, {s2} little, {s3} little Indians")


def lyric_end(s4, s5):
    print(f"{s4} little Indian boy{s5}")



lyric_main("One", "two", "three")
lyric_main("Four", "five", "six")
lyric_main("Seven", "eight", "nine")
lyric_end("Ten", "s")

'''
Keep unchanged content inside the function body
Keep changed content as arguments, pass to function
'''

print("")

lyric_main("Ten", "nine", "eight")
lyric_main("Seven", "six", "five")
lyric_main("Four", "three", "two")
lyric_end("One", "")


