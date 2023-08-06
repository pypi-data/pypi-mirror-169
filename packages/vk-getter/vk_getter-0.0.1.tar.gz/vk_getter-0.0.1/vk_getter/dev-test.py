from utils import print_posts_data, download_from_url
from getter import VKGetter

if __name__ == "__main__":
    vk_token = "vk1.a.rPuJjCAhHt88fQifhYvrQQ4-DgojMsuhKFIUD96x75YL0XqEabTWdK3TR0x1hXlnuC-DjNhUHDmlazJE1RiklYnWKOO0lxtWmo6mreHzxC3GycqGJMDQv7D4agy9CKEgvbS7cz2-n6gdZn-q0XA4mf7bt6Knvq5XmXyUyhEYhJQXTcVuNXBwGXxVrKbQiWWh"
    getter = VKGetter(vk_token)

    domain = "crawlic"
    posts = getter.get_latest_posts(group_domain="vk",
                                    count=1,
                                    include_pinned=False,
                                    allow_no_attachments=False,
                                    include_ads=False,
                                    include_copyright=False)
    print_posts_data(posts)
    #photo = posts[0].attachments.audio[0]
    #download_from_url(photo, "test", "dsa")
    getter.download_attachments(posts, path=domain)
