<template>
  <div class="mainPage">
    <h1>{{ msg }}</h1>
    <h2>h2 main page</h2>
    <prefNavigation></prefNavigation>

    <ul>
      <li v-for="planet in jsonInput">
        <button
          type="button"
          class="btn"
          @click="showModal">
          {{ planet.title }}
        </button>
      </li>
    </ul>
    <button type="button" @click="getLists">load data</button>
    <ul>
      <li v-for="item in list">
        {{ item }}
      </li>
    </ul>

    <modal
      v-show="isModalVisible"
      @close="closeModal"
    />







  </div>
</template>

<script>
import contentbox from './contentbox'
import prefNavigation from './prefNavigation'
import {jsonInput} from '../dataJSON'

export default {
  name: 'mainPage',
  data () {
    return {
      msg: "mainPage message",
      jsonInput,
      isModalVisible: false,
      list: {"1":"ich","2":"du","3":"er"},
    }
  },
  components: {
    modal: contentbox,
    prefNavigation
  },
  methods: {
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      },
      getLists() {
        fetch("http://localhost:5000")
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data);
          this.list = data;
        })
      },
    },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #mainPage {
    float: left;
  }
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
