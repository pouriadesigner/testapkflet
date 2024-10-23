from flet import *

body = Container(
    Container(
        Stack([
            Container(
                border_radius=11,
                rotate=Rotate(0.95 * 3.14),
                width=360,
                height=560,
                bgcolor="#33ffffff",
                

            ),
            Container(
                Container(
                    Column([
                        Container(
                            Image(
                                src="bird_3.png",
                                width=85,
                                
                                   
                            ),
                            padding=padding.only(130,20)
                        ),
                        Text(
                            "ورود",
                            width=360,
                            size=20,
                            weight=FontWeight.W_400,
                            text_align="center",
                            
                            
                        ),
                        Text(
                            "برای استفاده از نرم افزار وارد شوید",
                            width=360,
                            size=20,
                            weight="bold",
                            text_align="center",
                            
                            
                        ),
                        Container(
                            TextField(label="نام کاربری",hint_text="نام خود را وارد نمایید",color="#202020",prefix_icon=icons.EMAIL,width=280,height=60),
                            padding=padding.only(40,10)
                        ),
                        Container(
                            TextField(label="رمز عبور",hint_text="رمز عبور خود را وارد نمایید",color="#202020",prefix_icon=icons.LOCK,password=True,can_reveal_password=True,width=280,height=60),
                            padding=padding.only(40,10)
                        ),
                        Container(
                            TextButton(
                                "رمز عبور را فراموش کردم"
                            ),
                            padding=padding.only(40,10),
                            
                        ),
                        Container(
                            ElevatedButton(text="ورود",color="white",bgcolor=colors.AMBER_600,width=280),
                            padding=padding.only(40,10),
                        ),
                        Container(
                            Row([
                                Text("رمز عبور را فراموش کردید؟"),
                                TextButton("ارسال کد"),

                            ],),padding=padding.only(right=40,top=10),
                            rtl=True,
                        )

                    ])
                ),
                border_radius=11,
                width=360,
                height=560,
                bgcolor="#33ffffff",
                
            ),
        ]),
        padding=110,
        width=360,
        height=560,

    ),
    width=580,
    height=740,
    gradient=LinearGradient(["#333399","#ff00aa"]),
)

def main(page:Page):
    page.window_max_width = 580
    page.window_max_height = 740
    page.window_width = 580
    page.window_min_height = 740
    page.window_resizable = False
    page.padding = 0

    page.add(body)

app(target=main)
