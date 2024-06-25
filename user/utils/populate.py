from django.contrib.auth import get_user_model
import os
import django

def populate():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
    django.setup()

    print("here")
    json_data = [{"password": "qS8#`KnQA5NO=", "username": "agilbard0", "first_name": "Alix", "last_name": "Gilbard", "email": "agilbard0@xrea.com"},
                 {"password": "yL6>*pd6L8cqJ*f", "username": "lsaterthwait1", "first_name": "Lawrence",
                  "last_name": "Saterthwait", "email": "lsaterthwait1@nydailynews.com"},
                 {"password": "vZ9_H(.W+dK", "username": "ftoplin2", "first_name": "Feliza",
                 "last_name": "Toplin", "email": "ftoplin2@privacy.gov.au"},
                 {"password": "wO6#ctK2$t$5pG_", "username": "gwilde3", "first_name": "Gwenette",
                 "last_name": "Wilde", "email": "gwilde3@freewebs.com"},
                 {"password": "sJ4{K`8m2)'m|", "username": "mfilipczynski4", "first_name": "Maribel",
                 "last_name": "Filipczynski", "email": "mfilipczynski4@uol.com.br"},
                 {"password": "dF9$=mYjC", "username": "cbruinsma5", "first_name": "Cristina",
                 "last_name": "Bruinsma", "email": "cbruinsma5@nih.gov"},
                 {"password": "yV7=1*fN#+Dfs", "username": "fgirkin6", "first_name": "Franz",
                 "last_name": "Girkin", "email": "fgirkin6@ucoz.com"},
                 {"password": "pY3}2EVu", "username": "ilie7", "first_name": "Ivan",
                 "last_name": "Lie", "email": "ilie7@reddit.com"},
                 {"password": "yQ2_UgFH+9", "username": "bdenington8", "first_name": "Berna",
                 "last_name": "Denington", "email": "bdenington8@cnbc.com"},
                 {"password": "fE6,~BOV2<", "username": "ldefraine9", "first_name": "Llewellyn",
                 "last_name": "Defraine", "email": "ldefraine9@weebly.com"},
                 {"password": "cJ8(8cLm", "username": "ccallarda", "first_name": "Christye",
                 "last_name": "Callard", "email": "ccallarda@deviantart.com"},
                 {"password": "rM5_lB=?$>dk(", "username": "aconingb", "first_name": "Anny",
                 "last_name": "Coning", "email": "aconingb@yolasite.com"},
                 {"password": "mZ1!+1vSx}", "username": "nmariaultc", "first_name": "Nickie",
                 "last_name": "Mariault", "email": "nmariaultc@is.gd"},
                 {"password": "qT6)J+XHA", "username": "ctoxelld", "first_name": "Chas",
                 "last_name": "Toxell", "email": "ctoxelld@skyrock.com"},
                 {"password": "mH2(x$SZ|Vmlv", "username": "rdenerse", "first_name": "Riordan",
                 "last_name": "Deners", "email": "rdenerse@phoca.cz"},
                 {"password": "mJ9\"I=6D__CN#({", "username": "hslottf", "first_name": "Hans",
                 "last_name": "Slott", "email": "hslottf@prlog.org"},
                 {"password": "eM3)tds?Zm8`S(5", "username": "npaxmang", "first_name": "Northrop",
                 "last_name": "Paxman", "email": "npaxmang@narod.ru"},
                 {"password": "sT6@Q~O_p$c2xXb<", "username": "sasplinh", "first_name": "Stearn",
                 "last_name": "Asplin", "email": "sasplinh@123-reg.co.uk"},
                 {"password": "uS4>u{/M.,z", "username": "hhutcheonsi", "first_name": "Hayyim",
                 "last_name": "Hutcheons", "email": "hhutcheonsi@guardian.co.uk"},
                 {"password": "nX6%>jSb/WOwCT", "username": "mopenshawj", "first_name": "Marijn", "last_name": "Openshaw", "email": "mopenshawj@yahoo.com"}]

    User = get_user_model()

    for user_data in json_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        if created:
            user.set_password(user_data['password'])
            user.save()
            print(f"User {user.username} created successfully.")
        else:
            print(f"User {user.username} already exists.")
