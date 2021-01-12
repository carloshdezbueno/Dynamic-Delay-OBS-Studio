
import sys
import obswebsocket, obswebsocket.requests
import time as t
from multiprocessing import Process, Pipe, Queue
import PySimpleGUI as sg

def addDelay(record, stream, transition = 'Transition', delayScene = 'Delay', delay = 30):
    """Add delay function"""
    
    print("Adding delay")



    #Start recording with recording OBS
    record.call(obswebsocket.requests.StartRecording())
    

    #Mute Streaming OBS !!!Change names of sound sources
    stream.call(obswebsocket.requests.SetVolume('Cascos', 0.0))
    stream.call(obswebsocket.requests.SetVolume('Altavoces', 0.0))
    stream.call(obswebsocket.requests.SetVolume('Mic/Aux', 0.0))

    stream.call(obswebsocket.requests.SetCurrentScene(transition))

    #Pause program delayed time
    #(Tiene que haber un medio de video configurado de la misma para que no se vea raro)
    t.sleep(delay)

    #Reinicia el video ya que se reproduce de fondo
    stream.call(obswebsocket.requests.SetCurrentScene(delayScene))


    print("Delay added")

def removeDelay(record, stream, transition = 'removeDelayTransition'):
    """Remove delay function"""
    
    print("Removind delay")


    stream.call(obswebsocket.requests.SetCurrentScene(transition))

    #Stop recording with recording OBS
    record.call(obswebsocket.requests.StopRecording())

    
    t.sleep(0.3)

    #Unmute audio from Streaming OBS !!!Change names of sound sources
    stream.call(obswebsocket.requests.SetVolume('Cascos', 1.0))
    stream.call(obswebsocket.requests.SetVolume('Altavoces', 1.0))
    stream.call(obswebsocket.requests.SetVolume('Mic/Aux', 1.0))

    escenaActual = record.call(obswebsocket.requests.GetCurrentScene()).getName()

    stream.call(obswebsocket.requests.SetCurrentScene(escenaActual))

    print("Delay removed")


def sceneSyncronizer(transition = 'Transition', delayScene = 'Delay', removeDelayTransition = 'removeDelayTransition'):

    """syncronize Streaming OBS with Recording OBS. You only have to change scenes in Recording OBS so they are changed in Streaming OBS unless if you are with delay"""
    banned = [transition, delayScene, removeDelayTransition]

    #OBS websocket recording
    record = obswebsocket.obsws("localhost", 4444, "secret")
    record.connect()

    #OBS websocket stream
    stream = obswebsocket.obsws("localhost", 4445, "secret")
    stream.connect()

    transition = 'Transition'
    delayScene = 'Delay'
    removeDelayTransition = 'removeDelayTransition'

    banned = [transition, delayScene, removeDelayTransition]

    while True:
        actualRecordingScene = record.call(obswebsocket.requests.GetCurrentScene()).getName()

        actualStreamScene = stream.call(obswebsocket.requests.GetCurrentScene()).getName()

        if actualStreamScene not in banned and actualStreamScene != actualRecordingScene:
            stream.call(obswebsocket.requests.SetCurrentScene(actualRecordingScene))
        t.sleep(0.1)

def eventHandler(p_output, queue):

    """Used to comunicate with the different app threads"""
    
    #OBS websocket recording
    record = obswebsocket.obsws("localhost", 4444, "secret")
    record.connect()

    #OBS websocket stream
    stream = obswebsocket.obsws("localhost", 4445, "secret")
    stream.connect()

    withDelay = False

    while True:
        event = p_output.recv()

        if event == 'Exit' or event is None:
            if withDelay:
                removeDelay(record, stream, 'removeDelayTransition')
            break
        if event == 'addDelay':

            values = p_output.recv()
            try:
                if values == '':
                    addDelay(record, stream, 'Transition', 'Delay')
                else:
                    delay = int(values)
                    addDelay(record, stream, 'Transition', 'Delay', delay)
            except:
                sg.Popup('The delay must be an integer')
            withDelay = True
            
        if event == 'removeDelay':
            removeDelay(record, stream, 'removeDelayTransition')
            withDelay = False
        if event == 'cancel':
            break

    record.disconnect()
    stream.disconnect()
    sys.exit()

if __name__ == '__main__':
    #if I am without delay, the method of synchronizing scenes would be active
    #Hacer layout de config que guarde los datos

    #Crear archivo config
    defaultDelay = 30

    #Interface
    sg.ChangeLookAndFeel('LightGreen')
    layout = [[sg.Text('Dynamic Delay', size=(40, 1), justification='center')],
                [sg.Text(text='Delay:'), sg.InputText()],
                [sg.Button('Add delay', key='addDelay'), sg.Button('Remove delay', key = 'removeDelay', disabled=True)],
                [sg.Text(text='No delay', key='message', size=(40, 1))]
                ]
    window = sg.Window('Dynamic Delay', location=(800, 400))
    window.Layout(layout).Finalize()
    
    #Implementar con pipe para el correcto funcionamiento con 2 subprocesos
    
    p_output, p_input = Pipe()
    queue = Queue()

    pEventHandel = Process(target=eventHandler, args=((p_output),(queue)))
    pEventHandel.daemon = True
    pEventHandel.start()

    pSync = Process(target=sceneSyncronizer)
    pSync.daemon = True
    pSync.start()

    while True:
        event, values = window.Read()

        if not queue.empty():
            msg = queue.get()
            if msg == 'endingDelay':
                window.FindElement('message').Update('')

        if event == 'Exit' or event is None:
            p_input.send(event)

            pEventHandel.join()
            sys.exit()
            break
        if event == 'addDelay':
            p_input.send(event)
            p_input.send(values[0])

            window.FindElement('removeDelay').Update(disabled=False)
            window.FindElement('addDelay').Update(disabled=True)
            
            if values[0] == '':
                delayAdded = str(defaultDelay)
            else:
                delayAdded = values[0]

            window.FindElement('message').Update('You have ' + delayAdded + ' seconds delay')

        if event == 'removeDelay':
            p_input.send(event)

            window.FindElement('removeDelay').Update(disabled=True)
            window.FindElement('addDelay').Update(disabled=False)

            window.FindElement('message').Update('No tienes delay')
            
        if event == 'cancel':
            p_input.send(event)
            sys.exit()
