"""moduli sisältää pääohjelman"""
import config
from entities.user import User
from repositories.user_repository import UserRepository
from repositories.topic_repository import TopicRepository
from repositories.task_repository import TaskRepository
from repositories.result_repository import ResultRepository
from entities.topic import Topic

from dbcon import connection

def main():
    """pääohjelma, käynnistää käyttöliittymän"""
    #ei tee vielä mitään
    #tulee käynnistämään ensin tekstikäyttöliittymän, ja myöhemmin graafisen
    print("Pääohjelma ei tee vielä mitään, muuta kuin tulostaa terminaaliin")

    st1 = User(first_name="Eka", last_name="Testi", user_id ="tt", passwd="x", teacher=False)
    st2 = User(first_name="Toka", last_name="Kokeilu", user_id ="tk", passwd="1", teacher=False)
    th = User(first_name="Olli", last_name="Ope", user_id ="oo", passwd="1", teacher=True)    
    ur = UserRepository()
    ur.add_user(st1)
    ur.add_user(st2)
    ur.add_user(th)


    print(ur.all_students())
    print(ur.all_users())
    print(ur.user_details_by_user_id("tk"))
    print(ur.get_pk_id("tt"))
    print(ur.get_pwd(ur.get_pk_id("tk")))


    top = TopicRepository()
    topics = top.read_from_file()
    print(topics)
    top.update_db(topics)
    top.all_topics()
    print(top.id_by_topic("yhteenlasku"))
    print(top.topic_by_id(34))



    tsk = TaskRepository()
    tsk_list =  tsk.read_from_file()
    print(tsk_list)
    print(len(tsk_list))
    print(len(tsk_list[0]))

    tsk.update_db(tsk_list)


    rst=ResultRepository()
    rst.add_result(1,2, False)

    test_topic =Topic("yhteenlasku")


if __name__ == "__main__":
    main()
