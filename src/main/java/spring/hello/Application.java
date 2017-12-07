package spring.hello;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by wuzhiyong on 2017/12/7.
 */
public class Application {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("spring/hello/applicationContext.xml");
        context.getBean("hello",HelloWorld.class).sayHello();
    }
}
