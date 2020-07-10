<template>
  <div id="app">
      <wordcloud
      :data="defaultWords"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
      </wordcloud>
  </div>
</template>

<script>
import wordcloud from 'vue-wordcloud'
import io from 'socket.io-client';

export default {
  name: 'app',
  components: {
    wordcloud
  },
  created() {
    // `this` 指向 vm 实例
    console.log('myColors is: ' + this.myColors)
    
    const socket = io('http://127.0.0.1:5000');
    socket.on('connect', function(){
      console.log("--- connect -----")
      socket.emit('test_connect', {data: 'I\'m connected!'});
    });

    socket.on('connected',function(){
        console.log('connected');
    });

    socket.on('wordStats_msg', (data) => {
      console.log("---------- wordStats_msg event data --------")
      console.log(data)
      const allWords = JSON.parse(data["data"])
      console.log(allWords)
      const newWordStats = []
      for (const oneWord of allWords) {
        const oneName = Object.keys(oneWord)[0]
        const oneValue = oneWord[oneName]
        newWordStats.push({"name":oneName, "value":oneValue})
      }
      console.log(newWordStats)
      
      this.defaultWords.splice(0)

      for (const oneWord of newWordStats) {
        this.defaultWords.push(oneWord)
      }
    });
    socket.on('disconnect', function(){
      console.log("--- disconnect -----")
    });
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    }
  },
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      defaultWords: [{
          "name": "Cat",
          "value": 26
        },
        {
          "name": "fish",
          "value": 19
        },
        {
          "name": "things",
          "value": 18
        },
        {
          "name": "look",
          "value": 16
        },
        {
          "name": "two",
          "value": 15
        },
        {
          "name": "fun",
          "value": 9
        },
        {
          "name": "know",
          "value": 9
        },
        {
          "name": "good",
          "value": 9
        },
        {
          "name": "play",
          "value": 6
        }
      ]
    }
  }
}
</script>