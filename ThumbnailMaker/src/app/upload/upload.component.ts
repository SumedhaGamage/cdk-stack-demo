import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.scss']
})
export class UploadComponent implements OnInit {

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  selectedFile: File = null;

  onFileSelected(event){
    this.selectedFile = <File>event.target.files[0];
    
  }

  onUpload(){
    console.log('In onUpload');
    
    const fd = new FormData();
    fd.append('image', this.selectedFile, this.selectedFile.name)
    const data = {'image': this.selectedFile}
    console.log(data);
    
    this.http.post('https://93m87fqod5.execute-api.us-east-1.amazonaws.com/prod/', this.selectedFile, {
      headers: new HttpHeaders().set("content-type", "image/png")
    })
    .subscribe(res => {
      console.log(res['object_url']);
      
    })
    
  }

}
