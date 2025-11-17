from random import choice

frog="""
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttg cB ▆▅▅▅▆▆▅▆Bsttttttttttttttttttttttttttttttt
ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttgk(▆▆ lk               c█▇Lttttttttttttttttttttttttttt
ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttgk█▅ o             sss          k▆cttttttttttttttttttttttttt
ttttttttttttttttttttttttttttttttttgL  ihtttttttttttttttil▆█l          l▇▄▇(ok  LLL kB▆▇c      k▅ittttttttttttttttttttttt
ttttttttttttttttttttttttttttttc▅ c      kl ▆▆(kihth ▇█o           B▅ kLLLLLLLLLLLLLLLLL  ▇s     █ctttttttttttttttttttttt
ttttttttttttttttttttttttttth█         ss                      s█▅cLLLLLLLLLLLLLLLLLLLLLLLLB▇      kttttttttttttttttttttt
ttttttttttttttttttttttttttL▅s  s ▆l htttgo▆c                 ▅cLLLLLLLLLLLLLLLLLLLLLLLLLLLL ▆c    ▆itttttttttttttttttttt
ttttttttttttttttttttttttts▇  B█gtc▆▄▄▄▄▄█htlo            o▄lLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL l   k▇tttttttttttttttttttt
tttttttttttttttttttttttt ▆ s▆gh▇▄▄▄▄▄▄▄▄▄ ti█         s█▇ LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL█o    sttttttttttttttttttt
tttttttttttttttttttttttg▅ s▇tk▄▄▄▄▄▄▄▄▄▄▄ktol       l▅cLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL▆k  k█ttttttttttttttttttt
ttttttttttttttttttttttt█k Bkt▅▄▄▄▄▄▄▄▄▄▅Lt █      l▅sLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLk▇   ▅ttttttttttttttttttt
tttttttttttttttttttttt    llt(▄▄▄▄▄▄▄▅stt(B     c▅kLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL▇s  ▇gtttttttttttttttttt
tttttttttttttttttttttt k   █kth oosgttg        █lLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLBo  █Ltttttttttttttttttt
ttttttttttttttttttttth▆     c▆oithio▇ k         LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL   █Ltttttttttttttttttt
ttttttttttttttttttttti(                       LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL   ▇itttttttttttttttttt
ttttttttttttttttttttth                       lkLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLo   ▆htttttttttttttttttt
tttttttttttttttttttttg                       k▆LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL▆   ▆ttttttttttttttttttt
tttttttttttttttttttttL                         lLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL▆s  ▆ttttttttttttttttttt
ttttttttttttttttttth▇                          ▆kLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL▄   ▆gtttttttttttttttttt
ttttttttttttttttttg▆                             (LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL(B   (stttttttttttttttttt
ttttttttttttttttti▆                              k▅cLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLo▇    lotttttttttttttttttt
ttttttttttttttttL▆                                 c▅lLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL (     oltttttttttttttttttt
tttttttttttttttL▆                                      ▆cLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL (▆s      Bctttttttttttttttttt
ttttttttttttttL▆                                        s(▅(sLLLLLLLLLLLLLLLLLLLLLLLLLL B▅B         ▆gtttttttttttttttttt
tttttttttttttL▆           ▅▇▅▆B                             sB▇▅█Bc LLLLLLLLLLLLL kB▇▄ k           o(ttttttttttttttttttt
ttttttttttttL▆            ▆k   c▆(                                  sclBB(((((Blcs                 ▅httttttttttttttttttt
tttttttttttL▆          l▅▇█       (▇                                                              ▇Ltttgl▇Bttttttttttttt
tttttttttt ▆           ▅k            (                                                           █ktto▆k ( sgttttttttttt
ttttttttt ▆            (▅▅s          s▆                                                         (oto█      k▇ttttttttttt
tttttttts▆            ▅                B                               soB█▆▅▅▆▆▇▇▇▆▆▆█Bc      c h▇s      (▅▆otttttttttt
ttttttts▆              so(▇▅▇Bk                                  o ▅█o ggggggggggggggggggLB▇s    c           ▇Lttttttttt
ttttttk▇                       sl██s                        c█▆oigggggggggggggggggggggggggggggL L       sB▆(ittttttttttt
ttttts▇                                                 s(▅oggggggggggggggggggggggggggggggggggg (    (▅ohttttttttttttttt
tttts▇                                               s ▆sggggggggggggggggggggggggggggggggggggggglB igttttttttttttttttttt
tttk▇                                              B▆sgggggggggggggggggggggggggggggggggggggggggggs▇htttttttttttttttttttt
tts▇                                             █ gggggggggggggggggggggggggggggggggggggggggggggggg cttttttttttttttttttt
tg▅                                            █(ggggggggggggggggggggggggggggggggggggggggggggggggggg ▆gttttttttttttttttt
t▇c                                          l▇ggggggggggggggggggggggggggggggggggggggggggggggggggggggg otttttttttttttttt
 ▇                                          ▆kgggggggggggggggggggggggggggggggggggggggggggggggggggggggggs▇ttttttttttttttt
(o                                        k▆ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggi▆httttttttttttt
▆s                                       l ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg▆gtttttttttttt
▄                                       l(ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg▆gttttttttttt
▅                                      l(ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg▅htttttttttt
█k                                    c█ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggs tttttttttt
c                 o▇ lokkkcoB█▅▆B     ogggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg█Lttttttttt
t▅s                              c▆█s gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggcBttttttttt
ts█                                 l▆iggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggL█ttttttttt
ttl(                                  ( gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggi▆ttttttttt
tttB(                                  k▅igggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggL█ttttttttt
ttttc█                                   ▅Lggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggolttttttttt
ttttti▅s                                  ▅iggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg▅s ▇▇▇█▇▆▆c
ttttttt (                                 k▆gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg▇o       c▇o
tttttttth▇l                                llgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggL▅k        k▆L
tttttttttti▆l                               ▅gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg           B▄it
ttttttttttttg█                              c▇ggggggggggggggggggggggggggggggggggggggggggggggggggggggggL▇            s▆ t
ttttttttttttttto▆c                            so(▇▅( ggggggggggggggggggggggggggggggggggggggggggggggk▇▇kkkkkccolB ▆▅BLttt
tttttttttttttttttg(█                                 ▆sggggggggggggggggggggggggggggggggggggggsl▇▅B ttthtthtttttttttthttt
tttttttttttttttttttttgL                            c▅LhB(lcsLigghgggggggggggghgggLscl(▇▅▆ osgtttttttig LhiLLL LigLLiittt
ttttttttttttttttttttttttgB▅ c                     c▃▇htttttttthiLskcoooooccks Lghttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttgkB▇▅▅▇ (loks       sko▅ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
ttttttttttttttttttttttttttttttttttttttttttthgggghttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt


"""

women="""
⣿⢸⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⢿⣿⡇⡇⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⠄⢸⣿
⡟⢸⣿⣿⣭⣭⡭⣼⣶⣿⣿⣿⣿⢸⣧⣇⠇⢸⣿⣿⠈⣿⣿⣿⣿⣿⣿⡆⠘⣿
⡇⢸⣿⣿⣿⣿⡇⣻⡿⣿⣿⡟⣿⢸⣿⣿⠇⡆⣝⠿⡌⣸⣿⣿⣿⣿⣿⡇⠄⣿
⢣⢾⣾⣷⣾⣽⣻⣿⣇⣿⣿⣧⣿⢸⣿⣿⡆⢸⣹⣿⣆⢥⢛⡿⣿⣿⣿⡇⠄⣿
⣛⡓⣉⠉⠙⠻⢿⣿⣿⣟⣻⠿⣹⡏⣿⣿⣧⢸⣧⣿⣿⣨⡟⣿⣿⣿⣿⡇⠄⣿
⠸⣷⣹⣿⠄⠄⠄⠄⠘⢿⣿⣿⣯⣳⣿⣭⣽⢼⣿⣜⣿⣇⣷⡹⣿⣿⣿⠁⢰⣿
⠄⢻⣷⣿⡄⢈⠿⠇⢸⣿⣿⣿⣿⣿⣿⣟⠛⠲⢯⣿⣒⡾⣼⣷⡹⣿⣿⠄⣼⣿
⡄⢸⣿⣿⣷⣬⣽⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⢀⠉⠙⠛⠛⠳⠽⠿⢠⣿⣿
⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢄⣹⡿⠃⠄⠄⣰⠎⡈⣾⣿⣿
⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣽⣖⣄⣴⣯⣾⢷⣿⣿⣿
⣧⠸⣿⣿⣿⣿⣿⣿⠯⠊⠙⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⣿⣿
⣿⣦⠹⣿⣿⣿⣿⣿⠄⢀⣴⢾⣼⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾⣿⣿⣿⣿
⣿⣿⣇⢽⣿⣿⣿⡏⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⡿⣿⣛⣻⠿⣟⣼⣿⣿⣿⣿⢃
⣿⣿⣿⡎⣷⣽⠻⣇⣿⣿⣿⡿⣟⣵⣿⣟⣽⣾⣿⣿⣿⣿⢯⣾⣿⣿⣿⠟⠱⡟
⣿⣿⣿⣿⢹⣿⣿⢮⣚⡛⠒⠛⢛⣋⣶⣿⣿⣿⣿⣿⣟⣱⠿⣿⣿⠟⣡⣺⢿
"""



cat="""
　　　　　　　　 　　　　　　／ ¯¯｀フ
　　　　　　　　　,　'' ｀ ｀ / 　 　 　 !　 　
　　　　　　　 , ' 　　　　 レ　 _,　 -' ミ
　　　　　　　 ; 　 　 　 　 　`ミ __,xノﾞ､
　　　 　　 　 i　 　　　ﾐ　　　; ,､､､、　ヽ ¸
　　　 　　,.-‐! 　 　 　 ﾐ　　i　　　　｀ヽ.._,,))
　　 　　//´｀｀､　　　　 ミ　ヽ　　　　　(¯`v´¯)
　　　　| l　　 　｀ ｰｰ -‐''ゝ､,,)).　 　　 　 ..`·.¸.·´
"""
cat_memes="""
⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻
⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿
⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿
⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿
⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼
⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰
⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿
⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿
⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿
⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸
⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢸
"""
shrek="""
⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
"""


sea_women="""
                         ...                             |     |    |   |
    -`''-  _        ..########o...                       |     |    |   |
 _.'     `: \     ,##8#########8##o,,     (      (       `|    |    |   |
/ :  ___,-+-'   .#######8##8###8###8##,    )ailor )aturn  |    |    |   |
`-+-'     ;   ,#8###########8#8########,,                 `|   `|   |   `|
   `-...-'   :#88####8##8###########8###.,                 |    |  |'    |
            .HXX8X88X#8XX########XX8X8XX#;,                `|   |  |     |
           ,#O#X8888#88###########X####8X8,         _       `|  `\/'   ,/
          :8##88##X######8#8######X######8#:      _| |__     `|      ,/
         .######8##8####8)#)#(i#88####8####.:    |_   __|     `|    /
       .,#88##8#88###H8I~-_  _-~8+8##8####8#,:     | |___    __.----._
      :=#X##8#######,# ~-._()_.-~ ##########.,:    |  __ \   L__    __|
    .:I8##88####88#:;_--__    __--_,:#88#####),:   | |  \ |     |--|
   .:=8#XX#####88#LH =#O#\    /O##\i)##8######+:   | |  | \__  |'  `|
 .':###X888###8#8#O) \##@/    \##=/#H8###8####.,:  |_|  `\___| `|--|'
.':#####8####888L;;I,       |      #8###8##8###,.,              |  |
:.88Li######8#888#,H.     .__,    :8##88#####8##o:             |'  `|
:88X:##88##8##8#8##O8,           _8###########8#.8.           .|    |
8X#+#888#8##8#8#H.###8#,_      _-'8##=#####88#XX,o:           | \__/  _
X#..8#8##8##8888..8##8#8#-.__.-X#88##=8#####8#8#.,;           `.|__|-' |
'   HH8###;##8##,+888#L#|__  __|##88##;8###8##X'               ||(__- |'
_____                   |__()__|                _____          .|.:@#/_
\    `---.________.-----'      `-----._____.---'    /          ||._--' |
 \           oOOOOOOOOOOo__      ___oOOOOOOOOo    _/          | |(_----|
  \_.--_        oOOOOOOOOo -   --   oOOOOOOo __.-'            | |(_--__)
 _-:_-'           oOOOOOOOo        oOOOOOOo    `-_            | |.:(__ )
<::<_      _        oOOOOOOo       oOOOOo |       -_          `||.:@#_/
 ~-_:-__.-':'      xXXXxoOOOo ,|, oOOOoxXXXx _______\         |||.:@#|
    -_|    |        xXXXXXXXXx\|/.xXXXXXXXx  \ \             / `|.:@#|
      |   |'   _-.  xXXXXXxx--=O=--xxXXXXx|___| \           /  .|.:@#|
      |   |__-':/    xXXxxXXx'/|\`.XXxxxXX:.  '  \        ./  .:|.:@#|
      |     :::||    xxxXXXXx.'|`.xXXXXXxxx::.    \      /   .::|.:@#|
      |     :::||_  xxXXXXXXXx/'\_xXXXXXXXXx::.    \    /   .::/|.:@#|
      |    :::|' \`--xXXXXXXXx     xXXXXXx  \::.    \  /   .::/ |.:@#|
      |    :::|   \   xXXXXXX      xXXXx     \::.   /\/   .::/  |.:@#|
      |    ::|xx   \    xXx         xx        \::. /oO|  .::/   |.:@#|
     |'   .::|XXXXxx|    `          '|   xxxxx \::/OoOO\.::/    |.:@#|
     |    ::|XXXXXXX|                |xXXXXXx   \|oOOooOOOOo    |.:@#|
 ,-__|__ .::|XXXXXX/__              |_XXXXXx      OoooOoooooo   |.:@#|
 \ooooOOo::|XXXXXX/__ \,            | \XXXx       oOOOooOOOO    |.:@#|
  \OOOoooooo|XxoOOOo.\. \          / ./oOOoXXXXXx   oOOOoooo    |.:@#|
   |OOOOOOOO|oOOOOOOOo.\ \,       / /oOOOOOOoXXx       oOOo.    |.:@#|
   |oooooooo|OOOOOOOOOOo.\ \     / /oOOOOOOOOOOOo [ -Tim Park ] |.:@#|
"""

art="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡴⠶⠟⠓⣛⡺⠿⠖⠛⠚⠛⠳⠾⣒⡣⠴⣆⡤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠋⢁⡤⠄⠒⢉⣀⣠⣤⣤⣤⣤⣤⣤⣀⣀⠈⠁⠂⠌⡙⠊⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢎⠟⠀⣠⠞⣋⣤⡶⠿⠛⠛⠛⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣶⣤⡀⠉⠢⡈⠙⢕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⢀⣼⣿⠞⣉⣤⠔⠒⠉⠁⢀⡠⠔⠊⠉⠁⠠⣍⠹⠻⣿⣿⣿⣿⣷⣤⡈⢆⡀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣇⣤⣾⢟⣡⡾⠋⠁⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⢹⠱⡄⠀⠻⢿⣿⣿⣿⣿⣤⠱⡄⠈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⣤⢤⣿⣿⢑⣾⠋⠀⠀⡠⠀⠔⢁⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠈⢆⠀⠈⠻⣿⣿⣿⣿⣷⡘⣆⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢠⠇⣸⡟⢁⡜⠁⠀⣀⠞⠀⠀⠤⠀⣀⡈⠐⠂⠠⢀⡀⠀⠀⡇⠀⠈⡆⠀⠀⢻⣿⣿⣿⣿⣷⠈⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⡞⢀⡟⠠⠈⠀⣀⣼⠋⡰⠀⢠⠆⠀⠀⠈⠁⠒⠤⣀⠈⠑⠢⣀⠀⠀⢱⠀⠀⠀⢿⣿⣿⣿⣿⣯⠀⠀⢱⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠚⣄⣾⣹⠃⢠⣾⣟⡏⣰⠁⢠⠃⠀⠀⠀⠀⠀⠀⠀⡀⢉⠒⠤⣀⠙⠢⣈⡇⣀⠀⢺⣿⣿⣿⣿⣿⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣷⠇⢠⣿⣿⣼⢥⣷⣠⠇⠀⠀⢠⠀⠀⠀⡜⢀⠇⡼⣀⠀⠀⠑⠤⡀⠑⢼⠀⣇⢻⣿⣿⣿⣷⣀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⡠⡤⢺⠋⣸⡟⣠⣿⡏⢸⡃⢼⣇⡞⠀⠀⢠⠃⢀⢆⣼⢃⡞⣰⢻⡇⠀⠀⠀⠀⠉⠂⢸⠀⣯⡙⣿⣿⣿⣿⡙⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⡏⣰⣴⠃⢠⢿⡇⣽⢊⣧⣼⡆⡉⣿⡇⠀⠀⡞⢀⣎⣾⢻⣿⣾⣯⣟⢧⠀⠀⠀⡄⢠⠄⢸⢨⡗⣯⢾⡟⢹⡿⢿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡇⡁⠀⣾⣿⣏⣿⣸⣿⣿⣿⣯⣿⠀⣰⢺⠃⣼⣾⠟⣿⢏⡿⢻⣿⣞⠁⡀⢸⠃⣸⠂⣽⢰⣟⣾⡿⠀⡼⠀⣼⠀⢽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⡇⢰⣿⣿⢼⣿⣿⢉⣉⣿⣿⠿⡅⡏⣼⢣⣿⡣⠞⣱⣿⡁⢸⢌⡿⡔⠀⡿⢀⡿⢀⣿⣼⣿⣿⠃⣸⠃⢰⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠸⣾⣿⡏⢾⣿⡹⢾⣿⣿⣿⢀⣧⡧⢼⣿⠋⠀⠼⣿⣿⣷⣮⣾⡁⠹⣶⠇⣸⠇⣻⣿⡟⠉⠙⢲⡯⣤⡧⠤⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠲⠚⡶⢺⣟⣁⣠⢧⣿⠀⠀⠀⠀⢀⠀⢀⣼⠛⣿⣇⢺⡇⠀⠈⠛⠛⠃⠌⣿⠁⣾⣿⠀⠀⢀⣉⣿⣿⣿⣿⢰⣁⡞⢠⡟⢰⢿⣿⠁⠀⢠⠾⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⡇⢰⠁⣸⢿⣿⡇⢸⣿⣶⡼⣤⡀⠀⣆⠈⠁⠘⠛⠛⠿⠷⣀⠀⠀⠀⠀⠀⠹⡀⠘⣿⠁⠀⢸⣿⣿⣿⣿⡏⢐⡾⠁⡼⢡⡟⣾⠃⠀⡠⢁⢾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⠾⣠⣇⣼⣖⣻⣼⡿⠃⠀⣿⠈⢍⠙⠁⣠⡏⠁⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠁⠀⠘⠄⠀⠈⠙⠻⠿⠚⣣⠞⣁⣼⡣⣿⣼⠃⠀⢠⠥⣿⣿⡟⢙⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⠊⠀⢀⠁⠈⠁⠈⠁⠁⠀⢀⣼⠇⠀⠈⡦⠾⠛⠇⢀⡀⠀⢀⡀⠀⠀⠀⣸⠿⠶⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣢⡾⠃⣠⣿⡗⣽⡿⠃⠀⠀⡇⢀⣿⣿⠀⣾⣍⣰⣦⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠶⠶⡶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⠁⢀⠔⠁⠀⠀⠀⠀⠀⠀⢠⣿⠏⠀⢠⠊⠀⠀⠀⠀⢺⣃⡿⠯⠠⢷⣆⣼⣿⣷⡀⠐⠊⠛⠉⠀⠀⠀⠀⠀⠈⡽⠋⣠⣼⣿⠏⣽⣿⣇⠀⠀⠀⠳⣴⣿⡿⠛⠛⠁⠈⠁⠀⠀⢀⣠⣤⡶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣟⠀⠀⠀⠀⠀⠀⢀⡠⠄⠒⠋⠁⠀⠀⡃⠀⠀⠀⢀⠤⠋⠀⠀⠀⠀⣸⢣⣶⡟⠉⢹⢦⡄⢠⡤⠤⠴⠂⠒⢚⡟⣡⣾⣻⡟⣡⣾⣿⣿⣿⣷⣶⢶⡞⠉⢯⠀⠀⠀⠀⢀⣤⣴⣾⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⡈⠳⢦⣤⣉⣳⣿⠅⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⣠⠊⠀⠀⠀⣀⣀⣸⣳⠟⢋⣤⠶⡿⠘⡤⠇⠀⠐⠀⠄⠀⣾⣾⢳⣟⣿⣾⣿⣿⣿⣿⣿⡗⣿⢎⡇⠀⢿⣆⠀⠀⠀⣾⣷⢯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣆⠉⠓⠶⢭⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡶⠁⠀⣠⣶⣉⣤⠜⠋⣡⡶⠿⡁⡼⠁⠀⠘⠀⠀⠀⠀⠀⡼⢻⣷⣯⣿⣿⣿⣿⡿⣿⢻⣿⡝⣿⡎⣷⠀⠈⢿⢄⠀⠰⣏⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠸⢧⣝⠳⣦⣤⣤⡿⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠉⠀⠀⢠⡏⢯⠟⢁⣴⠞⠁⠠⣶⣺⢁⡆⠀⠀⠀⠀⠀⠀⡾⢡⣞⣿⣿⣿⠏⠀⠛⢿⣿⠈⣿⣿⡜⣷⢸⡄⠐⡼⡿⣦⠀⢷⠼⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀
⠀⠀⢠⠃⠀⠈⠙⠓⠛⡟⠁⠀⠀⠀⠀⠀⡠⠔⠉⠀⠀⠀⠀⣠⡿⢀⣯⣞⠽⠁⠀⠀⣠⣯⡽⠀⠇⠀⠀⠀⠀⢀⣠⣿⣫⢏⣼⣻⣇⠀⠀⠀⠀⠙⣄⣯⢹⣷⠚⣯⣇⠀⠹⡵⡈⠒⠾⣿⣽⣿⣿⣦⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀
⠀⠀⡾⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⣠⠔⠁⠀⢀⡠⠐⣒⣉⣩⣵⡶⠟⠛⠀⠀⠀⠀⠀⠀⠉⢗⣀⣀⡤⠴⣒⢻⣿⣟⣷⠃⣾⠳⠶⠚⢷⠒⠚⠁⠀⠀⠉⠛⢿⣯⡏⢿⣄⠀⠹⡀⠠⠀⠙⣿⣿⣿⣿⣷⠀⠲⠶⣚⠉⡁⠀⠀⠀⠀⠀⠀⠀
⠀⡸⠁⠀⠀⠀⠀⠀⡸⠀⣀⠔⠋⠀⠀⣴⣮⠷⢾⠿⠛⣩⣿⠏⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⣿⣀⣀⡀⠹⠛⠈⠁⢸⣿⣼⠃⣼⡇⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠋⣿⣄⠙⢆⠀⠡⠀⠐⠠⠈⠻⠟⠻⣿⣶⡄⠀⠀⠉⠉⠳⢦⡀⠀⠀⠀⠀
⢠⠁⠀⠀⠀⠀⠀⠀⢸⠋⠀⠀⢀⣴⠟⣣⢤⡏⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⢄⠈⠙⠛⠉⠙⠛⠃⠀⠀⠀⠀⠈⣿⡇⠸⣽⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠱⠀⠹⣿⢷⣀⠑⢄⢡⠀⠀⠀⠀⠀⡀⣼⣿⣿⣦⡀⠀⠀⠀⠀⠙⠂⠀⠀⠀
⡘⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣰⣿⠉⠀⢀⠀⠀⡀⢲⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⠙⢤⣿⡇⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡿⣎⠿⣷⡌⠹⣧⢦⡀⠀⠀⠙⣿⣜⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⡠⠎
⠁⠀⠀⠀⠀⠀⠀⠀⢸⠂⣼⡿⠏⠳⢮⠀⠀⠐⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠏⠀⠣⠈⠳⡝⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢿⠳⡜⣯⠡⣿⡆⠙⡆⠀⠀⠸⠙⢿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⢂⠀⠀⠀⠀⠀⠀⠀⣸⠠⣿⢧⢀⣰⡞⠀⢠⣀⡞⣿⠀⠀⠀⠀⠀⠀⠀⢀⡔⠂⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡟⠀⠀⠀⠀⠀⣷⡛⢲⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⡠⢻⡀⢠⣷⠀⠸⡆⠀⣠⠗⠚⠻⣿⣿⣿⠟⠃⠀⠀⣸⠆⠀
⠈⡄⠀⠀⠀⠀⠀⠀⠁⢘⣿⡛⢛⡙⠃⠠⠸⡅⢀⡇⠀⠀⠀⠀⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⢿⢯⡿⡇⠀⠀⠀⠀⢀⣿⠇⣸⠆⠰⣄⠀⠀⠀⠀⠀⠀⠀⣀⣿⠈⣧⠑⡇⠀⣿⡄⠀⣧⠎⠀⠀⠀⠀⢈⠟⠁⡠⠔⠊⠉⢻⣆⠀
⠀⠡⡀⠀⠀⠀⣀⠔⠚⠉⠹⡌⡅⠦⡑⡰⠐⡗⢻⡇⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⡀⢴⡾⠟⠋⠡⠞⢁⣾⣧⠃⠀⠀⠀⠀⢈⣼⣦⠿⣇⠀⠘⠄⠀⠀⠀⠀⠀⠀⣼⠏⠀⣿⡌⣧⠀⣿⠃⢀⠇⠀⠀⡀⠄⠘⠙⣖⠊⡀⠀⠒⠈⣻⠇⠁
⠀⠀⠑⠒⠒⠉⠀⠀⠀⠀⠀⢳⡈⢱⣥⡷⢿⣘⣼⣿⠀⠀⠀⠀⣸⠁⠀⠀⢀⣤⡾⠶⠦⠷⠀⠠⢀⣀⡾⣽⣿⠀⠀⠀⠀⠀⠀⣼⠁⠂⢼⡆⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⢰⢻⡇⣷⠀⣿⣤⡎⠀⠒⠉⠀⠀⠀⠀⠈⠯⠤⠤⠴⣾⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⣫⡅⡀⢴⣿⢿⣆⠀⠀⠀⡏⠀⠀⣠⠿⢯⡄⠀⡄⢈⣰⠴⠏⠹⢷⢮⣿⠀⠀⠀⠀⠀⠀⣏⠀⠖⣼⠟⣆⠀⠀⠀⠀⢀⠀⠀⠘⣤⢏⡾⣯⡗⢰⣿⣿⣇⠀⠀⢄⠀⠀⠀⠀⠀⢀⣀⣠⠶⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠯⢿⣟⣻⣦⣄⣀⡆⢠⣾⣿⣀⣸⡇⡘⣄⠢⢄⢳⠂⣀⣺⡄⣿⠀⠀⠀⠀⠀⢰⠃⣰⢺⡏⠀⢹⡀⠀⠀⠀⠈⠀⠀⠀⢹⠞⠀⡗⣧⡾⠁⠘⣿⣦⡀⢀⣉⡞⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡤⣉⣉⣛⣻⣷⣾⠿⣿⣻⠿⣟⡱⣮⢧⣄⡀⢋⠡⢉⢛⣿⡄⠀⠀⠀⠀⡞⣠⠃⣿⠃⠀⠀⡇⠀⠀⠀⠀⠃⠀⠀⢻⠀⢰⣿⠟⠀⠀⠀⠘⠮⣿⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠁⠀⠀⠀⠙⢶⣿⣿⣟⡶⣻⣍⠀⢉⡿⢠⠓⡌⠦⣿⡇⠀⠀⠀⣼⡵⠁⠀⣿⠀⢀⡞⣧⠀⠀⠀⠀⠀⠀⠀⠘⣄⡾⠋⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠗⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⠿⣿⣧⢶⡶⣿⢥⣫⣼⣃⠾⣇⠀⢀⣾⠟⠁⠀⠀⢹⡇⣼⣼⢻⡄⠀⠀⠀⠀⠀⠀⢠⠟⠈⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢽⣯⣌⣑⣄⣩⣍⣀⡭⠷⠛⠊⠉⢰⠃⠀⠀⠀⠈⣿⣿⢧⡿⣆⠀⠀⠀⠀⢀⠔⠋⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠭⣉⣉⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⣸⣿⡟⠀⢸⡄⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⢹⡟⢣⡀⠀⢷⡀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣮⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⢀⣾⡇⠀⠀⠑⠺⣇⠛⠀⠀⠀⠀⠀⠀⠀⠀⣠⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⣀⡠⠴⠋⠈⣇⠀⠀⠀⠀⠹⣃⠀⠀⠀⠀⠀⢀⣠⡞⠁⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠹⡦⠀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠑⢄⠀⠀⠀⠀⠈⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢿⡳⣤⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢮⣣⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠂⠱⡌⠛⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠻⠀⠀⠈⢳⣄⠙⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠹⣷⣄⠀⠉⠛⠿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠘⢿⣿⣦⣄⡀⠀⠉⠙⠻⠿⣶⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠻⣏⠳⢯⣗⡲⢤⣄⣀⡀⠈⠉⠛⠛⡿⠿⠷⠶⠶⠶⠶⠶⠶⠛⣛⡫⠭⠛⠋⠁⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣄⡈⠉⠓⠾⠧⣿⣿⣿⡶⠷⠒⠚⠒⠒⠚⠁⠃⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣻⠷⣶⣤⣤⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⢉⢟⡶⣮⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠈⢷⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""



scala="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⡑⢄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢮⣣⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠱⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣹⠀
⠀⠀⠀⠀⢀⣀⣀⣸⢧⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⣩⡤⠶⠶⠶⠦⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⡇
⠀⠀⠀⣰⣫⡏⠳⣏⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣶⣄⡀⠀⠀⢀⡀⠀⠀⠀⠀⠀⡀⡅⡇
⠀⠀⢰⡇⣾⡇⠀⠙⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⠿⠛⠻⢿⣶⣤⣍⡙⢿⣿⣷⣤⣾⡇⣼⣆⣴⣷⣿⣿⡇⡇
⠀⠀⢸⡀⡿⠁⠀⡇⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣯⠴⢲⣶⣶⣶⣾⣿⣿⣿⣷⠹⣿⣿⠟⢰⣿⣿⣿⠿⣿⣿⣿⠁
⠀⠀⠈⡇⢷⣾⣿⡿⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠹⣌⠳⣼⣿⣿⣿⣻⣿⣿⣿⣿⡇⠈⠁⢰⣿⣿⣿⣿⣶⣾⣿⣿⠀
⠀⠀⠀⣷⠘⠿⣿⡥⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠌⠉⣿⣿⣿⣿⣿⣿⠟⠃⠀⢀⡿⣿⣿⣿⣿⣿⣿⣿⡞⠀
⠀⠀⠀⢸⡇⠀⠹⠗⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⠟⠉⠉⠀⠀⠀⠈⢃⣿⣿⣿⣿⣿⣿⡻⠀⠀
⠀⠀⠀⠈⢧⠀⠀⠏⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⠀⠈⢳⠶⠞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠆⠀⠀⠊⠁⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⣼⣿⣀⡰⠀⠀⣤⣄⠀⠀⠀⠀⢹⣿⣿⣿⣿⢻⠀⠀⠀
⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⣿⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠙⣿⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⢠⣤⣶⣤⣀⠀⢀⣶⣶⣶⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠀⠻⣿⣿⣥⣤⣯⣥⣾⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠠⠀⠀⠀⠀⠈⣿⣿⣼⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⣠⣰⣄⡀⠀⢀⣀⣀⣛⣟⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠾⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠠⣄⣉⣉⣻⣿⣿⣿⣿⣿⣿⡟⠧⢄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠅⠀⠀⠀⠀⠘⠉⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠉⠓⠢⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⡄⠀⠀⢀⡑⠢⠄
"""
lst_art=[ scala, art, women, sea_women, shrek, cat, cat_memes, frog]
def photo():
    print(choice(lst_art))