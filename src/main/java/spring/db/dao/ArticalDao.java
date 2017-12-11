package spring.db.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import spring.db.model.Article;

/**
 * Created by wuzhiyong on 2017/12/8.
 */
@Repository
public class ArticalDao {

    private JdbcTemplate jdbcTemplate;

    public JdbcTemplate getJdbcTemplate() {
        return jdbcTemplate;
    }

    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public Article queryArticle(Integer id) {
        String sql = "select demo_id id,demo_title title,demo_author author, demo_date `date` from demo_tb where demo_id = ?";
        RowMapper<Article> rowMapper = new BeanPropertyRowMapper<>(Article.class);
        Article article = jdbcTemplate.queryForObject(sql, rowMapper, id);
        System.out.println(article);
        return article;
    }
}
