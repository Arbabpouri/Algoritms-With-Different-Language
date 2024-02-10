package main

import fmt


func main(){
	numbers := []
	for i := 0; i < count; i++ {
		for j := 0; j < count; j++ {
			if numbers[j] > numbers[j + 1] {
				temp := numbers[j]
				numbers[j] = numbers[j + 1]
				numbers[j + 1] = temp
			}
		}
	}

	fmt.println(numbers)
}