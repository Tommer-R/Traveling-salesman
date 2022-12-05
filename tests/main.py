from src import TSM

if __name__ == '__main__':
    agent = TSM(25, circle=False, render=1)
    route = agent.initial_route

    for i in range(100):
        cost = agent.route_distance(agent.random_route())
        print(f'{i}:    {cost}')

    agent.render_video()
