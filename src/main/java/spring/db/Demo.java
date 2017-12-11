package spring.db;

import org.springframework.jdbc.core.JdbcTemplate;

/**
 * Created by wuzhiyong on 2017/12/8.
 */
public class Demo {
    public static void main(String[] args) {
        JdbcTemplate t = new JdbcTemplate();
        t.query("", (rs, rowNum) -> {
            return "";
        });
    }
}
