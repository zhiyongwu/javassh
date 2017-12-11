package spring.db;

import org.junit.Assert;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import spring.db.dao.ArticalDao;
import spring.db.model.Article;

/**
 * Created by wuzhiyong on 2017/12/8.
 */

public class ArticleDaoTest {
    private static ApplicationContext context = new ClassPathXmlApplicationContext("/spring/hello/applicationContext.xml");
    private static ArticalDao articalDao = context.getBean("articleDao",ArticalDao.class);

    @Test
    public void test(){
       Article a = articalDao.queryArticle(1);
        Assert.assertNotNull(a);
    }
}
