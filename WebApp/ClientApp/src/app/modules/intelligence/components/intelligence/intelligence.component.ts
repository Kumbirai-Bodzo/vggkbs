import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Galleria } from 'primeng/galleria';
import { SweetAlertService } from 'src/app/application-shared/services/sweetAlert/sweetAlert.service';
import { IImage } from '../../interfaces/IImage';
import { IntelligenceService } from '../../services/intelligence.service';
import { interval, Subscription } from 'rxjs';
//import { Galleria } from 'primeng/galleria';
@Component({
  selector: 'app-intelligence',
  templateUrl: './intelligence.component.html',
  styleUrls: ['./intelligence.component.scss'],
})
export class IntelligenceComponent implements OnInit {
  uploadedFiles: any[] = [];
  @ViewChild('galleria') galleria: Galleria;
  galleryForm: FormGroup;

  uploading = false;
  uploaded = false;
  uplodingValue;
  predicting = false;
  //variables
  processedImagesList: IImage[];
  searchValue: string;
  subscription: Subscription;
  constructor(
    private intelligenceService: IntelligenceService,
    private sweetAlert: SweetAlertService
  ) {}

  ngOnInit() {
    //this.getProcessedImagesList();
    // setInterval(function () {
    //   console.log('fetching data...!');
    //   this.getProcessedImagesList();
    // }, 5000); //run this thang every 2 seconds

    const source = interval(20000);
    this.subscription = source.subscribe((val) => {
     this.getProcessedImagesList();
      console.log('fetching data...!');
    });
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
  uploadVideo(event): any {
    this.uploading = true;
    this.uplodingValue = 50;
    const formData: any = new FormData();

    formData.append('file', event.files[0], event.files[0].name);
    //formData.append('accommodation', this.accommodationId);
    console.log(event);
    // this.upLoadSingles(formData);

    this.intelligenceService.uploadVideo(formData).subscribe(
      (response) => {
        console.log(response);
        this.sweetAlert.success2('Uploaded video');
        this.uploading = false;
        this.uploaded = true;
        this.uplodingValue = 99;
      },
      (error) => {
        console.log(error);
        this.sweetAlert.error3('Failed uploading some images');
        this.uploading = false;
        this.uplodingValue = 0;
      }
    );
  }
  refresh() {
    //window.location.reload();
    this.getProcessedImagesList();
  }

  startPredictionProcess(): any {
    this.predicting = true;
    this.processedImagesList = null;
    this.intelligenceService.startPredictionProcess().subscribe(
      (response) => {
        console.log('my resoinse');
        console.log(response);
        // this.processedImagesList = response;

        this.predicting = false;
        this.sweetAlert.success('finished prediction');

        this.getProcessedImagesList();
      },
      (error) => {
        console.log(error);
        this.predicting = false;
        this.sweetAlert.error3('prediction failed');
      }
    );
  }
  getProcessedImagesList(): any {
   // this.predicting = true;
    this.processedImagesList = null;
    this.intelligenceService.getProcessedImages().subscribe(
      (response) => {
        console.log(response);
        this.processedImagesList = response;

        //this.predicting = false;
        this.sweetAlert.success('data successfully refreshed');
      },
      (error) => {
        console.log(error);
        //this.predicting = false;
        this.sweetAlert.error3('failed getting processed data');
      }
    );
  }
}
