package main

import (
    "fmt"; "log"; "net/http"
)

func main() {
    fmt.Println("Port 8080")
    http.Handle("/", http.FileServer(http.Dir(".")))
    err := http.ListenAndServe(":8080", nil)
    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}
