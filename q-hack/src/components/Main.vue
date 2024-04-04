<template>
  <v-container fluid class="fill-height hero">
    <v-responsive
      class="align-centerfill-height mx-auto" 
    >
      <div class="text-center">
        <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>

        <h1 class="text-h2 font-weight-bold">Exercise Enhancer</h1>
      </div>

      <div class="py-4" />

      <v-row>
        <v-col cols="8" offset="2">
          <v-card
            class="py-4"
            color="surface-variant"
            variant="rounded"
          >
            
            <div style="width: 210px; margin: 0 auto;">
              <v-icon>mdi-arrow-up-bold-box-outline</v-icon>
              <h2 style="margin-top: -28px; margin-left: 27px; padding-bottom: 10px;" class="text-h5 font-weight-bold" >Upload Your PDF</h2>
            </div>
         

            <v-row justify="center">
              <v-col cols="3" class="ml-5">
                <div style="border-radius: 25px; background-color: white; width: 310px;">
                  <input type="file" @change="handleFileUpload">
                </div>
              </v-col>
            

          </v-row>
          
          <v-row  justify="center">
            
              <v-col cols="3" >
              <v-btn elevation="8" color="blue" :disabled="this.show" size="x-large" class="mb-5 mr-0 " rounded="" @click="apiRequest">Make it engaging</v-btn>
              </v-col>

              <v-col cols="3">
              <v-btn elevation="8"  color="blue" size="x-large" :disabled="this.show" class="mb-5 ml-0 mr-2 " rounded=""   @click="apiRequest">Make it interactive</v-btn>
              </v-col>

              <v-col cols="3">
              <v-btn elevation="8"  color="blue" size="x-large" :disabled="this.show" class="mb-5 ml-3" rounded=""  @click="apiRequest">Make it AI-Resistant</v-btn>
              </v-col>

          </v-row>

          </v-card>
        </v-col>

    
      </v-row>
      <v-row>
        <v-col cols="6">
          <iframe
            v-if="pdfData"
            :src="pdfData"
            width="100%"
            height="600px"
            frameborder="0"
            scrolling="auto"
          ></iframe>
        </v-col>
        <v-col cols="6">
          <iframe
            v-if="pdfData"
            :src="pdfData"
            width="100%"
            height="600px"
            frameborder="0"
            scrolling="auto"
          ></iframe>
        </v-col>
      </v-row>
    </v-responsive>
    </v-container>

 </template>


<script>

  import axios from 'axios';

  export default{
    // Properties returned from data() become reactive state
    // and will be exposed on `this`.
    data: () => ({
        show: true,
        dialog: false,
        pdfData: null,
        pdfData2: '@/assets/AB.pdf',
        textExtracted: '',
        textpdf: ''
    }),
    // Methods are functions that mutate state and trigger updates.
    // They can be bound as event handlers in templates.
    methods: {
      handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.readPdfFile(file);
      }
      this.show = false;
      this.dialog = true;
      },
      readPdfFile(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.pdfData = e.target.result;
        };
        reader.readAsDataURL(file);
      },
    async handleFileInput(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = async () => {
          const buffer = reader.result;
          const text = await parse(buffer);
          this.textExtracted = text.text;
        };
        reader.readAsArrayBuffer(file);
        console.log(this.textExtracted);
      }
    },
    async gptRequest(imageUrl, level, language) {
        try {
          const response = await axios.post(
            PROXY+'https://api.openai.com/v1/chat/completions',
            {
              model: 'gpt-4-vision-preview',
              messages: [
                {
                  role: 'user',
                  content: [
                    { type: 'text', text: `Du erhälst von mir ein arbietsblatt mit aufgaben. Erstelle mir eine neue version des arbeitsblattes mit aufgaben, die deutlich schwierieger von einem LLM gelöst werden können. ':':`},
                    { type: 'text', text: this.textpdf },
                  ],
                },
              ],
            },
            {
              headers: {
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
                'Content-Type': 'application/json',
                'origin': 'https://gigolingo.com'
              },
            }
          );

          const res = response.data; // Modify based on API response structure

          return res;
        } catch (error) {
          console.error('Error in generateMemeCaption2 function: ', error);
          return null;
        }
    },
    apiRequest(){
      axios
      .get('127.0.0.1:8000/text/')
      //.post('127.0.0.1:8000/extract-text/', {pdf: this.pdfData})
      .then(response => console.log(response))
      //.then(response => (this.pdfData2 = response.data))
    }
  
    
  },
 }

</script>


<style scoped>
.hero {
  background: url('../assets/fractal-2880199_1920.jpg');
  background-size: cover;
  height: 100vh;
}
.black{
  background-color: gray;
}
</style>