import { Component,OnInit,SimpleChange,SimpleChanges,ViewChild } from '@angular/core'; 
import { HttpClient, HttpClientModule } from '@angular/common/http'
import { Chart } from 'chart.js';
import Config from 'chart.js/dist/core/core.config';
import { UIChart } from 'primeng/chart';


@Component({ 
	selector: 'app-root', 
	templateUrl: './app.component.html', 
	styleUrls: ['./app.component.css'] 
})

export class AppComponent {
  @ViewChild('chart') chart: UIChart | undefined; 
	title = 'XX'; 
  mychart: any;
  
  constructor(private http:HttpClient) {};

  categorias: Object = {
    'comida': ['cereais','milho','vegetais'],
    'produtos': ['shirt','casaco','oculos'],
    'veiculos': ['carros','motos','caminhao']
  }

  produtos: Object = {
    'produtos' : ['cerais','shirt','veiculos'],
  }
  
  marcas: Object = {
    'cerais' : ['cereal1','ceral2','ceral3'],
    'shirt' : ['shirt1','shirt2','shirt3'],
    'veiculos' : ['veiculos1','veiculos2','veiculos3'],
  }
  
  resultado: string = "comida";
  first_temp: any;
  second_temp: any;
  last_temp: any;
  django_object: any;
  final_data_source:any = [];
  outro:any = []
  
  firstEvent(value: any){
    this.first_temp = this.categorias[value.target.value as keyof typeof this.categorias];
    console.log(this.first_temp);
  }

  secondEvent(value: any){
    let temp: String = value.target.value;
    this.second_temp = [temp.concat('1'),temp.concat('2'),temp.concat('3')];
   console.log(value.target.value);  
  }

  lastEvent(value: any){
    this.last_temp = value.target.value;
    // console.log(this.last_temp);
    Object.entries(this.django_object).forEach(([key, value], index) => {
      if(key == this.last_temp){
        this.final_data_source = value;

        this.basicData.datasets[0].data = this.final_data_source
        console.log(this.basicData.datasets[0].data)
      }
    });
  }
  
  updateGraphFunction(){
    if(this.final_data_source !== null){
      this.basicData.datasets[0].data = this.final_data_source;
      this.chart?.refresh();
      setTimeout(() => {
        this.chart?.refresh();
      },1)
      return this.basicData;
    }
    return this.basicData;
  }

  ngOnInit(): void{
    this.django_object = this.http.get("http://127.0.0.1:8000/home/").subscribe(
      data => this.django_object = data
    )
    this.basicData = this.updateGraphFunction()
  }
  
  ngOnChanges(changes: SimpleChanges): void{
    if(changes['inputData'].currentValue){
      setTimeout(() =>{
        this.chart?.refresh();
      }
      ,1)
    }
    this.chart?.initChart()
  }



basicData = { 
  labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril'],
  
  datasets: [ 
    {
      label: 'Sales by month for:', 
      backgroundColor: 'blue', 
      data: [500, 320, 410, 520, 600, 600, 600] 
    }, 
  ],
  
};

basicOptions = { 
  plugins: { 
    legend: { 
      labels: { 
        color: '#black'
      } 
    } 
  }, 
  scales: { 
    x: { 
      ticks: { 
        color: '#black'
      }, 
      grid: { 
        color: 'rgba(0,0,0,0.4)'
      } 
    }, 
    y: { 
      ticks: { 
        color: '#black'
      }, 
      grid: { 
        color: 'rgba(0,0,0,0.4)'
      } 
    } 
  },
};
}
