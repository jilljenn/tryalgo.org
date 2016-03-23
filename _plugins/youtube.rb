module Jekyll
  class Youtube < Liquid::Tag

    def initialize(name, id, tokens)
      super
      @id = id.strip
    end

    def render(context)
      %(<iframe src="//www.youtube.com/embed/#{@id}?cc_load_policy=1" style="width: 100%; min-height: 400px"></iframe>)
    end
  end
end

Liquid::Template.register_tag('youtube', Jekyll::Youtube)