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

---

### 14. NSOperationQueue 와 GCD Queue 의 차이점을 설명하시오.


---
### 15. GCD API 동작 방식과 필요성에 대해 설명하시오.

---

### 16. Global DispatchQueue 의 Qos 에는 어떤 종류가 있는지, 각각 어떤 의미인지 설명하시오.

---

### 17. iOS 앱을 만들고, User Interface를 구성하는 데 필수적인 프레임워크 이름은 무엇인가?

UIKit입니다. UIKit는 Cocoa Touch Framework 안에 속해있습니다.

UIKit는 UI와 관련된 기능을 담당합니다.

UIKit 클래스 중 UIResponder에서 파생된 클래스나 사용자 인터페이스에 관련된 클래스는 애플리케이션의 메인 스레드(혹은 메인 디스패치 큐)에서만 사용.

---

### 18. Foundation Kit은 무엇이고 포함되어 있는 클래스들은 어떤 것이 있는지 설명하시오.

Foundation Kit은 Cocoa Touch framework에 포함되어 있는 프레임워크 중 하나입니다. 

UI와 관련된 기능을 담당하는 UIKit와는 달리 UI를 제외한 앱의 기본적인 기능을 담당합니다.
예를 들어, String, Int 등의 원시 데이터 타입과 운영체제 서비스 및 URLSession 같은 네트워크 기능을 포함하고 있습니다.

---

### 19. Delegate란 무언인가 설명하고, retain 되는지 안되는지 그 이유를 함께 설명하시오.

Delegate는 클래스나 구조체가 자신의 책임이나 임무를 다른 인스턴스에게 위임하는 디자인 패턴입니다.

Retain는 메모리가 제 때 해제되지 않아 누수되는 의미인데, Delegate는 ViewController, 즉 Class간에 작업이 대다수이기 때문에 Call By Reference이므로 순환참조로 인해 Retain이 생길 가능성이 있습니다. 이를 방지하고자 약함 참조 weak를 사용합니다.

---

### 20. NotificationCenter 동작 방식과 활용 방안에 대해 설명하시오.



---

### 21. UIKit 클래스들을 다룰 때 꼭 처리해야하는 애플리케이션 쓰레드 이름은 무엇인가?

UIKit의 대부분의 구성 요소는 nonatomic(서로 연결된)으로 기술되어 있으며, 이는 Thread-safe하지 않다 것을 의미합니다. UIKit에서 모든 속성을 Thread-safe하게 디자인하는 것은 UIKit이 너무 방대한 프레임워크이기 때문에 비현실적입니다. 

모든 View의 변경 사항은 즉시 변경되는것이 아니라 현재 RunLoop의 끝에서 다시 그려짐. 만약 모두 main Thread에서 작업하지 않는다면, View의 layout이 제대로 동작한다고 보장할 수 없습니다.

---

### 22. App Bundle의 구조와 역할에 대해 설명하시오.



---

### 23. 모든 View Controller 객체의 상위 클래스는 무엇이고 그 역할은 무엇인가?

UINavigationController, UITableViewController, UITabBarController 등 모든 View Controller는 UIViewController를 상속받습니다.

UIViewController는 뷰의 계층 구조를 관리합니다.

---

### 24. 자신만의 Custom View를 만들려면 어떻게 해야하는지 설명하시오.

Xib 파일을 이용하거나

Programmatically 하게 코드로 작성하여 UIView 객체를 초기화합니다.

---

### 25. View 객체에 대해 설명하시오.



---

### 26. UIView 에서 Layer 객체는 무엇이고 어떤 역할을 담당하는지 설명하시오.

layer 타입은 CALayer입니다. CA가 있다시피, Core Animation 프레임워크에 있습니다. 

UIView는 레이아웃, 터치 이벤트 등 많은 작업을 하지만, 사실은 뷰 위에 컨텐츠나 애니메이션을 그리는 행위는 직접하지 않고 Core Animation에 위임을 합니다.

---

### 27. UIWindow 객체의 역할은 무엇인가?

UIWindow는 직접적으로 시각적인 내용을 나타내지는 않지만 화면을 구성하는 모든 뷰들의 부모가되는 컨테이너 역할을 하는 객체입니다.

---

### 28. UINavigationController 의 역할이 무엇인지 설명하시오.

UINavigationController는 스택처럼 화면들을 쌓아서 화면간 이동을 관리하는 컨테이너입니다.

---

### 29. TableView를 동작 방식과 화면에 Cell을 출력하기 위해 최소한 구현해야 하는 DataSource 메서드를 설명하시오.

인덱스마다 어떤 셀을 사용할지 반환하는 cellForRowAt이 있고, 섹션마다 표시할 셀의 개수를 반환하는 numberOfRowsInSection이 있습니다.

---

### 30. 하나의 View Controller 코드에서 여러 TableView Controller 역할을 해야 할 경우 어떻게 구분해서 구현해야 하는지 설명하시오.



---

### 31. setNeedsLayout와 setNeedsDisplay의 차이에 대해 설명하시오.

setNeedsLayout은 뷰의 위치와 크기를 업데이트하는 layoutSubviews를 다음 업데이트 사이클에 호출하도록 예약하는 메서드입니다. setNeedsDisplay는 뷰의 내용을 그리는 draw 메서드를 다음 업데이트 사이클에 호출하도록 예약하는 메서드입니다.


---