# python을 이용한 Mic, LED 제어

라즈베리파이에 연결한 모듈을 제어하기위한 예제코드이다.

## LED_control.py

wakeup, think, speak 세가지 형식의 LED 제어 테스트를 위한 python code

    pixel.wakeup()
    
pixel_ring.wakeup()을 실행 후  think나 speak를 실행해야 LED가 밝게 동작한다.

동작방식은 각 함수가 동작하면 end_LED()가 동작할때까지 LED가 동작한다. 변수로 n을 입력받아 sleep하여 동작의 지속시간을 컨트롤했다.

## LED_test.py

LED_control을 테스트하기위해 작성한 코드로 command를 입력하고 동작할 시간 n을 입력하면 테스트가 가능하다.

## decibel_measurement.py

일정크기 이상의 소리가 들어오면 LED를 동작하도록 작성한 코드이다.

주의할 점은

    data = np.fromstring(stream.read(CHUNK), dtype = np.int16)

이 부분에서 read 할때 일정시간안에 읽지 않으면 overflow가 발생한다는 점이다.

예를 들면 if문에서 LED.think() 함수를 호출하여 LED가 동작한 후 다시 read하면 overflow 발생

=> LED_think()가 동작하는 동안도 stream에는 버퍼가 쌓이는 중이다. 만약 stream.stop_stream()을 사용하지 않고 동작하게 하고싶으면
CHUNK 변수의 값을 크게 해주면 된다.(추천하지는 않음)
