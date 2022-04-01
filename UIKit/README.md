### 1. Bounds와 Frame의 차이점을 설명하시오.
이 둘은 View의 위치와 크기를 나타내는 데 그 기준이 다릅니다. 
위치부터 보자면, Frame은 상위 뷰를 기준.. 즉, Super View를 기준으로 위치를 잡습니다. Bounds는 자기 자신을 기준으로 위치를 잡습니다. 한 마디로 View를 생성 하게되면 bounds의 origin는 항상으로 0으로 초기화 됩니다.

그 다음, 크기를 말씀드리겠습니다. frame는 자기 자신 View 영역을 모두 감싸는 사각형을 기준으로 크기를 잡습니다. bounds는 자기 자신 View 영역 자체를 기준으로 크기를 잡습니다.

---

### 2. 실제 디바이스가 없을 경우 개발 환경에서 할 수 있는 것과 없는 것을 설명하시오.

제가 경험한 바로는 카메라를 사용할 수 없습니다.

---

### 3. 앱의 콘텐츠나 데이터 자체를 저장/보관하는 특별한 객체를 무엇이라고 하는가?

먼저, UserDefaults 입니다.
UserDefaults는 key-value 형태로 데이터를 관리합니다. 특히, 사용자 설정같은 기본적인 정보를 저장하기 유리합니다. 그렇지만, 앱을 삭제하면 저장된 값이 사라진다는 단점이자 장점이 있습니다.

그 다음은, CoreData입니다.
Coredata는 데이터베이스와 같이 저장하며, 앱을 삭제해도 영구히 남는다는 특징을 가지고 있습니다. 

---

### 4. 앱 화면의 콘텐츠를 표시하는 로직과 관리를 담당하는 객체를 무엇이라고 하는가?

UIViewController 입니다. UIViewController는 View 게층구조를 관리하고 뷰를 그리는 로직을 담고 있습니다.

---

### 5. App thinning에 대해서 설명하시오.

앱 안에는 실행 가능한 코드와 리소스로 구성되어 있습니다. 앱을 사용자한테 제공할 때 서로 다른 디바이스를 위한 다양한 앱 번들을 만들고 전달하는 과정을 App thinning이라 합니다.

---

### 6. 앱이 시작할 때 main.c 에 있는 UIApplicationMain 함수에 의해서 생성되는 객체는 무엇인가?

UIApplicationMain이 실행되면 싱글톤 UIApplication 객체를 생성됩니다.
또한, 

---

### 7. @Main에 대해서 설명하시오.

Swift 5.3 부터는 @main(@UIApplicationMain 대신에)을 사용한다.
UIKit 기반 앱의 main entry point이다.

---

### 8. 앱이 foreground에 있을 때와 background에 있을 때 어떤 제약사항이 있나요?

foreground는 App이 실행되어 사람들에게 보여지고 있는 상태이며, background는 엡에서 벗어난 상태입니다. 
background 상태에서는 사용자에게 이벤트를 받기 어려우며, 공유 시스템 리소스 해제를 해제합니다.

---

### 9. 상태 변화에 따라 다른 동작을 처리하기 위한 앱델리게이트 메서드들을 설명하시오.

`func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool`  
애플리케이션이 실행된 직후 사용자의 화면에 보여지기 직전에 호출, 어플리케이션이 최초 실행될 때 호출되는 매소드

`application:willFinishLaunchingWithOptions`  
어플리케이션이 최초 실행될 때 호출되는 매소드

`application:didFinishLaunchingWithOptions`  
어플리케이션이 실행된 직후 사용자의 화면에 보여지기 직전에 호출

`applicationDidBecomeActive`  
어플리케이션이 Active 상태로 전환된 직후 호출

`applicationWillResignActive`  
어플리케이션이 Inactive 상태로 전환되기 직전에 호출

`applicationWillEnterForeground`  
어플리케이션이 Active 상태가 되기 직전에, 화면에 보여지기 직전의 시점에 호출

`applicationWillTerminate`  
어플리케이션이 종료되기 직전에 호출

`connectingSceneSession`  
scene이 만들어질때 새로운 configuration적용하기위해.

`didDiscardSceneSessions`  
유저가 scene을 제거했을때.


---

### 10. 앱이 In-Active 상태가 되는 시나리오를 설명하시오.

Foreground에서는 Active 상태와 In-Active 상태가 존재합니다. In-Active 상태가 될려면 전화, 시리, Alert 등 사용자로부터 이벤트를 받지 못할 상황이여야 합니다.

---

### 11. scene delegate에 대해 설명하시오.

iOS 13부터 iOS는 Multiple Window를 지원하기 시작했습니다.

이로 인해 하나의 App이 여러 개의 Scene을 갖을 수 있습니다.

Scene delegate가 각 화면마다 만들어져 App Delegate가 가지고 있던 UI LifeCycle와 관련된 메소드를 처리하게 됩니다.

---

### 12. UIApplication 객체의 컨트롤러 역할은 어디에 구현해야 하는가?


---

### 13. App의 Not running, Inactive, Active, Background, Suspended에 대해 설명하시오.

Not running은 앱이 아직 실행되지 않은 상태,

Inactive는 실행되고 있지만 이벤트를 받을 수 없는 상태,

Background는 백그라운드에서 코드를 실행중인 상태, 

Suspended는 백그라운드에서 코드를 실행중이지 않은 상태를 의미합니다.

---

### 번외, App 실행 과정

main 함수가 실행
main 함수는 UIApplicationMain함수를 호출
UIApplicationMain함수는 앱의 본체에 해당하는 객체인 UIApplication 객체를 생성한다.
nib파일을 사용하는 경우나, Info.plist 파일을 읽어들여 파일에 기록된 정보를 참고하여 그외에 필요한 데이터를 로드한다.
앱 델리게이트 객체를 만들고 앱 객체와 연결하고 런루프를 만드는 등 실행에 필요한 준비를 한다.
실행 완료를 앞두고 앱 객체가 앱 델리게이트에게 application:didFinishLaunchingWithOptions: 메시지를 보낸다.