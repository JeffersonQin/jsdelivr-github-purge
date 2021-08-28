# jsdelivr-github-purge

通过遍历本地的`repo`文件夹，获取文件目录信息，自动访问`purge.jsdelivr.net`来刷新`cdn`。

忽略`.`开头的文件夹

## 配置

配置文件示例：

```
{
	"path": "/mnt/d/CodeSpace/blog-asset/", 
	"repo": "JeffersonQin/blog-asset",
	"version": "latest"
}
```

注：记得`path`最后要加上`/`
