<?php

$orig_cookie = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw';

$orig_data = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function calc_key($cookie, $data) {
    $key = json_encode($data);
    $text = base64_decode($cookie);
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$key = calc_key($orig_cookie, $orig_data);
echo $key;
// qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq

$new_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$key = 'qw8J';

function xor_encrypt($data, $key) {
    $text = json_encode($data);
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$new_cookie = base64_encode(xor_encrypt($new_data, $key));
echo $new_cookie;
// ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK
