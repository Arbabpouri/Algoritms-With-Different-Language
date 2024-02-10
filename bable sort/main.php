<?php
    $numbers = [9, 5, 4, 1, 7, 94, 513, 574, -1, -200, 0];

    for ($i = 0; $i < 20; $i++){
        for ($j = 0; $j < 20 - $i - 1 ; $j++){
            if ($numbers[$j] > $numbers[$j + 1]){
                $temp = $numbers[$j]
                $numbers[$j] = $numbers[$j + 1]
                $numbers[$j + 1] = $temp
            }
        }
    }

    echo($numbers);

?>