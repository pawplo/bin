package main

import (
    "mime"; "fmt"; "log"; "net/http"
)

func main() {
    fmt.Println("Port 8080")

    mime.AddExtensionType(".wgsl", "text/wgsl")
    mime.AddExtensionType(".svg", "image/svg+xml")

    http.Handle("/", http.FileServer(http.Dir(".")))
    err := http.ListenAndServe(":8080", nil)
    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}
