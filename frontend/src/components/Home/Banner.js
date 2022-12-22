import React from "react";
import logo from "../../imgs/logo.png";
import agent from "../../agent";

const Banner = (props) => {
  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div>
          <span>A place to </span>
          <span id="get-part" onClick={() => {document.getElementById("search-box").style.display = "inline";}}>get</span>
           <input
                      style={{display: 'none'}}
                      id="search-box"
                      type="text"
                      placeholder="What is that your truely desire?"
                      value={props.search}
                      onChange={(ev) => {
                        ev.preventDefault();
                        if (ev.target.value && ev.target.value.length > 2)
                        props.onSetSearch(
                          ev.target.value,
                          agent.Items.all(0, ev.target.value)
                        );
                      }}
                    />
          <span> the cool stuff.</span>
        </div>
      </div>
    </div>
  );
};

export default Banner;
