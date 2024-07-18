def check_replicaset_range(Step):
    print("Step:", Step, " 確認是否超出範圍")
    Step += 1


def new_pid_alo(Step):

    print("Step:", Step, " 獲取指標")
    Step += 1
    print("Step:", Step, " 計算伸縮比例")
    Step += 1
    # 是否超過調整值
    print("Step:", Step, " 確認是否超過調整值")
    Step += 1

    # 是擴容還是下降
    if 1 == 1:
        if 1 == 1:
            quick_up(Step)

        else:
            slow_down(Step)
    else:
        pass

    # 修改值


def quick_up(Step):
    # 判斷當前要用哪種伸縮方式

    if 1 == 1:
        print("Step:", Step, " 進行快速伸縮")
        Step += 1

    else:
        print("Step:", Step, " 進行快速伸縮")
        Step += 1

    check_replicaset_range(Step)

    # 回傳回去


def slow_down(Step):
    # 判斷當前要用哪種伸縮方式

    if 1 == 1:
        print("Step:", Step, " 進行緩慢縮減")
        Step += 1

    else:
        print("Step:", Step, " 進行快速縮減")
        Step += 1

    check_replicaset_range(Step)

    # 回傳回去


new_pid_alo(1)
