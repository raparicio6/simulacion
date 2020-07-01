import matplotlib.pyplot as plt
import random
import queue


class Request:
    def __init__(self, body, headers):
        self.body = body
        self.headers = headers


def does_request_arrive():
    return random.random() < 1/40


def is_request_processed():
    return random.random() < 1/30


working_seconds = 1000
requests_interaction_miliseconds = 10
steps = int((working_seconds * 1000) / requests_interaction_miliseconds)
q = queue.Queue()
states = []

for i in range(steps):
    queue_size = q.qsize()
    states.append(queue_size)
    if queue_size > 0 and is_request_processed():
        q.get_nowait()

    if does_request_arrive():
        request = Request('example body', 'example headers')
        q.put_nowait(request)

states_strings = list(map(str, states))
plt.plot(states_strings, color='green', alpha=0.5, lw=1.8)
plt.xlabel('Instantes')
plt.ylabel('Solicitudes')
plt.show()

plt.hist(states_strings, color='green', ec='black', alpha=0.5, bins=20)
plt.xlabel('Estados')
plt.ylabel('Solicitudes')
plt.show()

steps_without_requests_to_process = len(list(filter(lambda n: n == 0, states)))
print('Porcentaje de tiempo que el servidor se encuentra sin procesar solicitudes: {}%'.format(
    float((steps_without_requests_to_process) / len(states)) * 100))
