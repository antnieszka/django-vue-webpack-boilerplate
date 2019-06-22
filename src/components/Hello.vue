<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="getStats(this)" class="klekle">Update stats</button>
  </div>
</template>

<script>
var getStats = function(self) {
  self.$http.get("/api/stats/").then(
    response => {
      self.msg = "Hello ID: " + response.body.hello;
      console.log(response);
    },
    response => {
      console.warn(response);
    }
  );
};

export default {
  data() {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: "Hello There!"
    };
  },
  methods: {
    getStats: function() {
      return getStats(this);
    }
  },
  mounted: function() {
    getStats(this);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.hello {
  background-color: aquamarine;
}
.klekle {
  border: solid 5px red;
  padding: 10px;

  &:hover {
    border-color: blue;
  }
}
</style>
