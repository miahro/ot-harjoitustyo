"""moduli sisältää plot_user_details - funktion"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from config import DIFFICULTY_RANGE


def plot_user_details(user, details):
    """näyttää käyttäjän tulosten yksityiskohdat erillisessä ikkunassa

    Args:
        user: käyttäjän tiedot
        details: tulosten yksityiskohdat resultservice.user_details
            metodin palauttaman sanakirjana
    """    
    diff_range = DIFFICULTY_RANGE
    col_dict = dict(zip(diff_range, plt.cm.tab10.colors[:len(diff_range)]))
    topics = details['all'].keys()
    x = DIFFICULTY_RANGE
    wd = 0.5
    fig, ax = plt.subplots(4, 2, num=f"Oppilaan {user['first_name']} {user['last_name']} tulokset")

    for idx, top in enumerate(topics):
        ax[idx, 0].pie(details['all'][top][1], labels=details['all'][top][0],
                       autopct=lambda p: f"{p*sum(details['all'][top][1])/100 :.0f}", colors=[col_dict[key] for key in details['all'][top][0]])
        ax[idx, 0].title.set_text(f"{top} yhteensä per vaikeustaso")

        ax[idx, 1].bar(x=details['correct'][top][0]-wd/2,
                       height=details['correct'][top][1], width=wd, label="oikein")
        ax[idx, 1].bar(x=details['fail'][top][0]+wd/2,
                       height=details['fail'][top][1], width=wd, label="väärin")
        
        ax[idx, 1].set_xticks(x)
        ax[idx, 1].set_xlabel("vaikeustaso")
        ax[idx, 1].set_ylabel("kpl")
        ax[idx, 1].legend()
        ax[idx, 1].title.set_text(f"{top}, oikein ja väärin")
        ax[idx, 1].yaxis.set_major_locator(MaxNLocator(integer=True))


    fig.set_figheight(10)
    fig.set_figwidth(16)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4,hspace=0.9)
    plt.show()
